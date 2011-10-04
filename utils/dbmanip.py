from genericpath import exists
import DBMigrations
import os

__author__ = 'dennis'

import sqlite3
import ini
        
import imp
import os
MODULE_EXTENSIONS = ('.py', '.pyc', '.pyo')

def CreateDB():
    if not exists(ini.DB_NAME):
        backupFileName = os.path.join(os.path.dirname(__file__),ini.BACKUPFILE)
        fp = open(backupFileName)
        fileCont = fp.read().split(";\n")

        conn = sqlite3.connect(ini.DB_NAME)
        cu = conn.cursor()

        try:
            for sql in fileCont:
                cu.execute(sql)

            conn.commit()
            
            #Migreren naar latere versie indien nodig
            DoMigration()
            
        except sqlite3.OperationalError:
            print sql
            conn.rollback()
            
    else:
        #bestaat, versie nagaan en indien nodig updaten
        DoMigration()
        
        
def DoMigration():
    conn = sqlite3.connect(ini.DB_NAME)
    cu = conn.cursor()

    try:
        cu.execute('Select * from schema_info')
        
    except sqlite3.OperationalError as error:
            #wss nog geen versie info, dus ook deze tabel aanmaken
            cu.execute('CREATE TABLE [schema_info] ([schemaVersion] INTEGER  PRIMARY KEY NULL)')
            conn.commit()
            cu.execute('insert into schema_info (schemaVersion) values (0)')
            conn.commit()
            
            DoMigration() #recursief
            
    else:
        #tabel is in orde dus kijken of er niet moet geupgrade worden.
        currentDBVersion=0
        res = cu.fetchone()
        
        if res:
            currentDBVersion = res[0]
            
        #zoek de hoogste versie in de package
        migrations=sorted(package_contents("DBMigrations"))
        migrations.remove('__init__')
                
        versions = []
        for migration in migrations:
            versions.append((int(migration.split("_")[1]),migration))
            
        for version in versions:
            if currentDBVersion < version[0]:
                exec("from DBMigrations import "+version[1])
                exec(version[1]+".Up()")
                cu.execute('update schema_info set schemaVersion=?',(version[0],))
                conn.commit()
                print "Upgraded to {0:s}".format(version[1])
            

def package_contents(package_name):
    file, pathname, description = imp.find_module(package_name)
    if file:
        raise ImportError('Not a package: %r', package_name)
    # Use a set because some may be both source and compiled.
    return set([os.path.splitext(module)[0]
        for module in os.listdir(pathname)
        if module.endswith(MODULE_EXTENSIONS)])
    
if __name__ == '__main__':
    CreateDB()

from genericpath import exists
import imp
import ini
import os
import sqlite3
##import MySQLdb

__author__ = 'dennis'

        
MODULE_EXTENSIONS = ('.py', '.pyc', '.pyo')

def CreateDB():
    if (ini.DB_TYPE == "Sqlite3"):
        if (not exists(ini.DB_NAME_SQLITE3)):

            fileCont = readBackupFile()
    
            conn = sqlite3.connect(ini.DB_NAME_SQLITE3)
            cu = conn.cursor()
    
            try:
                for sql in fileCont:
                    print sql
                    if sql:
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
##                
##    elif (ini.DB_TYPE == "MySQL"):
##        fileCont = readBackupFile()
##        
##        conn = MySQLdb.connect(ini.DB_SERVER_MYSQL, ini.DB_NAME_MYSQL, ini.DB_USER_MYSQL, ini.DB_PWD_MYSQL)
##        cu = conn.cursor()
##        
##        cu.execute("SET sql_mode='ANSI_QUOTES';")
##        
##        for sql in fileCont:
##            
##            print "ORG: "+sql
##            
##            sql = sql.replace("[","")
##            sql = sql.replace("]","")
##            sql = sql.replace("AUTOINCREMENT","AUTO_INCREMENT")
##            sql = sql.replace(",'''",",'")
##            sql = sql.replace("'''","")
##            print sql
##            if sql:
##                cu.execute(sql)
##
##        conn.commit()
            
        
def DoMigration():
    conn = sqlite3.connect(ini.DB_NAME_SQLITE3)
    cu = conn.cursor()

    try:
        cu.execute('Select * from schema_info')
        
    except sqlite3.OperationalError as error:
            #wss nog geen versie info, dus ook deze tabel aanmaken
            cu.execute('CREATE TABLE [schema_info] ([schemaVersion] INTEGER PRIMARY KEY NULL)')
            conn.commit()
            cu.execute('insert into schema_info (schemaVersion) values (0)')
            conn.commit()
            
            DoMigration() #recursief
            
    else:
        #tabel is in orde dus kijken of er niet moet geupgrade worden.
        currentDBVersion = 0
        res = cu.fetchone()
        
        if res:
            currentDBVersion = res[0]
            
        #zoek de hoogste versie in de package
        migrations = sorted(package_contents("DBMigrations"))
        migrations.remove('__init__')
                
        versions = []
        for migration in migrations:
            versions.append((int(migration.split("_")[1]), migration))
            
        for version in versions:
            if currentDBVersion < version[0]:
                exec("from DBMigrations import " + version[1])
                exec(version[1] + ".Up()")
                cu.execute('update schema_info set schemaVersion=?', (version[0],))
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
    
def readBackupFile():
    
    backupFileName = os.path.join(os.path.dirname(__file__), ini.BACKUPFILE)
    fp = open(backupFileName)
    allLines = fp.read()
    oneString = "".join(allLines)
    oneString = oneString.replace("\n", " ")
    oneString = oneString.replace("\r", " ")
    fileCont = oneString.split(";")
    
    return fileCont
    
if __name__ == '__main__':
    CreateDB()

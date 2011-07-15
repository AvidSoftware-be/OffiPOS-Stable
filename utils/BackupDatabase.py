import sqlite3, os
import StringIO
import ini
import codecs

__author__ = 'dennis'

import sqlite3

DB_FILE = "..\\BaronPOS.db"
NEW_DB_FILE = "Backup.sql"
FILETYPES = dict(sql=1, db=2)

def getTableDump(db_file, table_to_dump):
    conn = sqlite3.connect(db_file)

    cu = conn.cursor()
    cu.execute("select sql from sqlite_master where type='table' and name='" + table_to_dump + "'")
    sql_create_table = cu.fetchone()[0]

    return sql_create_table.replace("\r","") + ";\n"


def getViewDump(db_file, viewToDump):
    conn = sqlite3.connect(db_file)

    cu = conn.cursor()
    cu.execute("select sql from sqlite_master where type='view' and name='" + viewToDump + "'")
    sql_create_view = cu.fetchone()[0]

    return sql_create_view.replace("\r","") + ";\n"


def getInsertStatements(db_file, table_name):
    retList = []
    conn = sqlite3.connect(db_file)

    cu = conn.cursor()
    # Build the insert statement for each row of the current table
    res = cu.execute("PRAGMA table_info('%s')" % table_name)
    column_names = [str(table_info[1]) for table_info in res.fetchall()]
    q = "SELECT 'INSERT INTO \"%(tbl_name)s\" VALUES("
    q += ",".join(["'||quote(" + col + ")||'" for col in column_names])
    q += ")' FROM '%(tbl_name)s'"
    res = cu.execute(q % {'tbl_name': table_name})
    for row in res:
        retList.append("%s;\n" % row[0])

    return retList


def BackupDB(srcDb, destFile, fileType=FILETYPES["sql"]):
    
    dbSQL = []
    conn = sqlite3.connect(srcDb)
    cur = conn.cursor()
    cur.execute("select name, type from sqlite_master where NOT name = 'sqlite_sequence'")
    result = cur.fetchall()
    for line in result:
        dbSQL.append("DROP " + line[1].upper() + " IF EXISTS {0:};\n".format(line[0]))
        if line[1] == 'table':
            dbSQL.append(getTableDump(srcDb, line[0]))
            for line in getInsertStatements(srcDb, line[0]):
                dbSQL.append(line)
        else:
            dbSQL.append(getViewDump(srcDb, line[0]))

    if fileType == FILETYPES["sql"]:
        f = open(destFile,"w")
    else:
        conn = sqlite3.connect(destFile)
        cur = conn.cursor()

    for stat in dbSQL:
        try:
            if fileType == FILETYPES["db"]:
                cur.execute(stat)
            else:
                f.write(stat)

        except sqlite3.OperationalError as error:
            print error.message

    if fileType == FILETYPES["db"]:
        f.close()
    else:
        conn.commit()

if __name__ == '__main__':
    BackupDB(DB_FILE, NEW_DB_FILE,FILETYPES["sql"])
    





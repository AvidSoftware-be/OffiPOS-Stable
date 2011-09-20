from genericpath import exists
import os

__author__ = 'dennis'

import sqlite3
import ini

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
        except sqlite3.OperationalError:
            print sql
            conn.rollback()


if __name__ == '__main__':
    CreateDB()
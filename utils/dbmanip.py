from datetime import date, datetime
from genericpath import exists
import os
from DataModel.Customer import Customer

__author__ = 'dennis'

import sqlite3
import ini

def CreateDB():
    if not exists(ini.DB_NAME):
        backupFileName = os.path.dirname(__file__)+"\\Backup.sql"
        fp = open(backupFileName)
        fileCont = fp.read().split(";\n")

        conn = sqlite3.connect(ini.DB_NAME)
        cu = conn.cursor()
        for sql in fileCont:
            cu.execute(sql)

        conn.commit()


if __name__ == '__main__':
    CreateDB()
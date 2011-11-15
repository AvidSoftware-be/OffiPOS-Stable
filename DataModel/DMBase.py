import ini
import sqlite3
import MySQLdb

class DMBase(object):
    def __init__(self):
        if ini.DB_TYPE == "Sqlite3":
            self._conn = sqlite3.connect(ini.DB_NAME_SQLITE3, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            self._conn.text_factory = str
            
        elif ini.DB_TYPE == "MySQL":
            self._conn = MySQLdb.connect(ini.DB_SERVER_MYSQL, ini.DB_NAME_MYSQL, ini.DB_USER_MYSQL, ini.DB_PWD_MYSQL)
            
        else:
            print "DB_TYPE invalid in ini.py!"

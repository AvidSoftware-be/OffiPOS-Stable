import sqlite3, ini

def Up():
    
    conn = sqlite3.connect(ini.DB_NAME)
    cu = conn.cursor()
    
    cu.execute('''CREATE TABLE [day_totals] (
[entryNo] INTEGER  PRIMARY KEY AUTOINCREMENT NOT NULL,
[dateRegistered] TIMESTAMP  NULL,
[vatCode] INTEGER  NULL,
[priceVatIn] REAL  NULL)''')
    
    conn.commit()


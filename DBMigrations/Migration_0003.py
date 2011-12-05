import sqlite3, ini

def Up():
    
    conn = sqlite3.connect(ini.DB_NAME_SQLITE3)
    cu = conn.cursor()
    
    try:
    
        cu.execute('''CREATE TABLE "customer_remarks" (
    "entryNo" INTEGER PRIMARY KEY AUTOINCREMENT,
    "customerNo" INTEGER,
    "remark" TEXT
);''')
        conn.commit()
        
    except sqlite3.OperationalError as e:
        print e.message
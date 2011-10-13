import sqlite3, ini

def Up():
    
    conn = sqlite3.connect(ini.DB_NAME)
    cu = conn.cursor()
    
    try:
    
        cu.execute('''ALTER TABLE [product] ADD COLUMN treatAsOption INTEGER DEFAULT 0''')
        
        cu.execute('''UPDATE product SET treatAsOption=1 WHERE id >= 346 AND id <= 372 ''')
        
        conn.commit()
        
    except sqlite3.OperationalError as e:
        print e.message
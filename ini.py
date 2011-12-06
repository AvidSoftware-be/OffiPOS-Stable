from datetime import date
import os, sys

__author__ = 'dennis'

SERVICEURL = "http://localhost:8000" #not used

LOG_FILENAME = 'BaronPOS.log'
BACKUPFILE = 'Backup.sql'

#DB_TYPE = "Sqlite3" # or "MySQL"
DB_TYPE = "MySQL"

#Sqlite3 DB Settings
#----------------------
DB_NAME_SQLITE3 = 'C:\\BaronPOS\\BaronPOS.db'#'/home/dennis/Aptana Studio 3 Workspace/BaronPOS/src/BaronPOS.db'
#DB_NAME = os.path.join(os.path.dirname(sys.argv[0]), 'BaronPOS.db')

#MySQL settings
#------------------------
DB_SERVER_MYSQL = "localhost"
DB_NAME_MYSQL = 'BaronPOS'
DB_USER_MYSQL = 'BaronPOS'
DB_PWD_MYSQL = 'BaronPOS'

#Klantenkaart systeem
#-----------------------
LOYALTYCARD_EURO_PER_POINT = 3 #per hoeveel euro krijgt men een punt
LOYALTYCARD_POINTS_FOR_BONUS = 100 #hoeveel punten moet men hebben voor een bonus
LOYALTYCARD_BONUS_AMOUNT = 15 #hoeveel euro bonus krijgt men
LOYALTYCARD_STARTING_POINTS = 20 #hoeveel punten krijgt men voor het intekenen


# systeem settings, niet veranderen
#-------------------------
MINDATE = date(1900, 1, 1)

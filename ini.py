from datetime import date

__author__ = 'dennis'

SERVICEURL = "http://localhost:8000"

LOG_FILENAME = 'BaronPOS.log'
#DB_NAME = 'D:\\Dev\\BaronPOS\\baronpos\\BaronPOS.db'
DB_NAME = '\\\\kassa\\C\\BaronPOS\\BaronPOS.db'
BACKUPFILE = 'Backup.sql'

LOYALTYCARD_EURO_PER_POINT = 3
LOYALTYCARD_POINTS_FOR_BONUS = 100
LOYALTYCARD_BONUS_AMOUNT = 15
LOYALTYCARD_STARTING_POINTS = 20

MINDATE = date(1900, 1, 1)
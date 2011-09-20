from datetime import date
import os, sys

__author__ = 'dennis'

SERVICEURL = "http://localhost:8000"

LOG_FILENAME = 'BaronPOS.log'
#DB_NAME = 'D:\\Dev\\BaronPOS\\baronpos\\BaronPOS.db'
DB_NAME = '/home/dennis/Aptana Studio 3 Workspace/BaronPOS/src/BaronPOS.db'
#DB_NAME = os.path.join(os.path.dirname(sys.argv[0]), 'BaronPOS.db')
BACKUPFILE = 'Backup.sql'

LOYALTYCARD_EURO_PER_POINT = 3
LOYALTYCARD_POINTS_FOR_BONUS = 100
LOYALTYCARD_BONUS_AMOUNT = 15
LOYALTYCARD_STARTING_POINTS = 20

MINDATE = date(1900, 1, 1)

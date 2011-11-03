from datetime import date
import os, sys

__author__ = 'dennis'

SERVICEURL = "http://localhost:8000"

LOG_FILENAME = 'BaronPOS.log'
DB_NAME = 'C:\\BaronPOS\\BaronPOS.db'
#DB_NAME = '/home/dennis/Aptana Studio 3 Workspace/BaronPOS/src/BaronPOS.db'
#DB_NAME = os.path.join(os.path.dirname(sys.argv[0]), 'BaronPOS.db')
BACKUPFILE = 'Backup.sql'

LOYALTYCARD_EURO_PER_POINT = 3 #per hoeveel euro krijgt men een punt
LOYALTYCARD_POINTS_FOR_BONUS = 100 #hoeveel punten moet men hebben voor een bonus
LOYALTYCARD_BONUS_AMOUNT = 15 #hoeveel euro bonus krijgt men
LOYALTYCARD_STARTING_POINTS = 20 #hoeveel punten krijgt men voor het intekenen

MINDATE = date(1900, 1, 1)

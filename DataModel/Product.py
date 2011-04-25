

__author__ = 'dennis'

import sqlite3

class Product:

    def __init__(self, id, price, name, group):
        self.price = price
        self.id = id
        self.name = name
        self.group = group
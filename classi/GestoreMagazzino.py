from PyQt5.QtCore import QObject
import mysql
import mysql.connector
import credenzialiDb
class GestoreMagazzino():
    def __init__(self):
        self.db = mysql.connector.connect(
            host = credenzialiDb.host,
            username = credenzialiDb.user,
            password = credenzialiDb.password,
            database = credenzialiDb.database
        )
        self.cursor = self.db.cursor()
        self.elementiMagazzino

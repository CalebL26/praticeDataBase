import sqlite3
conn = sqlite3.connect('databasefile.db')
cr = conn.cursor()

cr.execute("""
           CREATE TABLE IF NOT EXISTS movies
           id INTEGER PRIMARY KEY, 
           title TEXT, 
           director TEXT, 
           year INTEGER, 
           genre TEXT
           """)
#Table should be created with those attributes/columns names
# Here we are going to deal just with the database creation through python
import sqlite3

connection = sqlite3.connect("sample.db") # NEI

table = "CREATE TABLE people (id integer primary key, name TEXT, surname TEXT)"
cursor = connection.cursor()
cursor.execute(table) # here I am excuting the table creation
connection.commit()
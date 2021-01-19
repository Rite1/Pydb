from pydb import pydb

# SQL Tabel syntax
user_tabel_syntax = """
'CREATE TABLE Users
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL);
"""

# Pydb class object
ExampleModel = pydb.Pydb("../example.db", user_tabel_syntax)

# functions

# makes connection with the file that is passed during the defination of object
ExampleModel.make_connection()

# makes the tabel, in your case it will make a user tabel
ExampleModel.make_table()
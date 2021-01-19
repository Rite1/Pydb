import sqlite3

class Pydb():
    def __init__(self, filename, tabel_sql_syntax):
        self.filename = filename
        self.tabel_sql_syntax = tabel_sql_syntax

    def make_connection(self):
        global connection
        connection = sqlite3.connect(self.filename)
        print("Made Connection")

    def make_table(self):
        connection.execute(self.tabel_sql_syntax)
        print("Made Tabel")

    def insert(self, insert_command):
        connection.execute(insert_command)
        print("Inserted")

    def select(self, select_command):
        connection.execute(select_command)
        print("selected")

    def update(self, update_command):
        connection.execute(update_command)
        print("Updated")

    def delete(self, delete_command):
        connection.execute(delete_command)
        print("Deleted")
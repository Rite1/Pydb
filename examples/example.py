from pydb import pydb

# SQL Tabel syntax
user_tabel_syntax = """
CREATE TABLE Users
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL);
"""

# Pydb class object
ExampleModel = pydb.Pydb("example.db", user_tabel_syntax)

# commands
insert_command = """
INSERT INTO Users (ID,NAME,AGE) \
      VALUES (1, 'Rite', 32)
"""

select_command = """
SELECT * from Users
"""

update_command = """
UPDATE Users
SET NAME = 'Rite Changed'
WHERE ID = 1
"""

delete_command = """
DELETE FROM Users WHERE id=1;
"""

# functions

# makes connection with the file that is passed during the defination of object
ExampleModel.make_connection()

# makes the tabel, in your case it will make a user tabel, you have to run this command only once as we have to create table only one time
ExampleModel.make_table()

# inserting value into tabel
ExampleModel.insert(insert_command)

# select something from table
ExampleModel.select(select_command)

# updates a value
ExampleModel.update(update_command)

#deletes a value
ExampleModel.delete(delete_command)
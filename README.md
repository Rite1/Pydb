# Pydb
A Python module to work with database, based on sqlite3.

### Example
```python
from pydb import pydb

user_tabel = """
CREATE TABLE Users
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL);
"""

object = pydb.Pydb("filename.db", user_tabel)

object.make_connection()
object.make_table()

insert_command = """
INSERT INTO Users (ID,NAME,AGE) \
      VALUES (1, 'Rite', 32)
"""

object.insert(insert_command)
```

### Want to contribute?
#### [join](https://discord.gg/YpjyrMFNm7) the discord server

### Future updates?
- we will provide docs (currently working on docs)
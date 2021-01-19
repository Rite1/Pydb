# file with pre defined models

user_model = """
CREATE TABLE User
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         PASSWORD       VARCHAR(50)     NOT NULL);
"""

blog_model = """
CREATE TABLE BlogPost
         (ID INT PRIMARY KEY     NOT NULL,
         TITLE           TEXT    NOT NULL,
         AUTHOR          TEXT    NOT NULL,
         CONTENT         VARCHAR(50)     NOT NULL);

"""
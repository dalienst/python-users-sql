from db import dbcursor, db

create_user_table_query = """
CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    password VARCHAR(100)
)
"""

# dbcursor.execute(create_user_table_query)
# db.commit()

dbcursor.execute("SHOW TABLES")
for x in dbcursor:
    print(x)

dbcursor.execute("DESCRIBE users")
for x in dbcursor:
    print(x)
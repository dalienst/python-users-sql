from db import dbcursor

select_users = "SELECT * FROM users"
dbcursor.execute(select_users)
for x in dbcursor.fetchall():
    print(x)
from db import dbcursor, db


def create_account():
    print("Welcome to Users Place")
    print("Fill in your details")
    print("***********************************************")
    username = input("Enter a username: ")
    first_name = input("Enter your firstname: ")
    last_name = input("Enter your lastname: ")
    password = input("Enter a password: ")
    insert_user = """
    INSERT INTO users
    (username, first_name, last_name, password)
    VALUES ( %s, %s, %s, %s )
    """
    user_records = [
        username,
        first_name,
        last_name,
        password,
    ]
    dbcursor.execute(insert_user, user_records)
    db.commit()
    print("Account Created Successfully")


# print(create_account())


def login():
    # username = input("Enter a username: ")
    # password = input("Enter a password: ")
    username_query = """
    SELECT username FROM users
    """
    password_query = """
    SELECT password FROM users
    """
    dbcursor.execute(username_query)
    for x in dbcursor:
        print(x)
    password_data = dbcursor.execute(password_query)
    # if username == username_data and password == password_data:
    #     print("Logged in")
    # else:
    #     print("Invalid Credentials")


print(login())

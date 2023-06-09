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
    return "Account Created Successfully"


# print(create_account())


# def login_user():
#     username_query = """
#     SELECT username FROM users
#     """
#     password_query = """
#     SELECT password FROM users
#     """
#     username = input("Enter a username: ")
#     usernames = dbcursor.execute(username_query)
#     for usernames in dbcursor:
#         if "".join(usernames) != username:
#             print("Invalid username")
#             break
#         else:
#             print("Username login valid")
#             password = input("Enter a password: ")
#             password_data = dbcursor.execute(password_query)
#             for password_data in dbcursor:
#                 if "".join(password_data) == password:
#                     return "Logged in successfully"
#                     break
#                 else:
#                     return "Login failed!!!"
#                     break


# print(login_user())


def login():
    """
    function to login the user
    the function fails if the username and password do not match
    """

    user_query = "SELECT username, password FROM users"

    users = dbcursor.execute(user_query)
    for users in dbcursor.fetchall():
        user = users

    username = input("Enter a username: ")
    if username not in user:
        print("User account does not exist")
    else:
        print("Username login valid")

    password = input("Enter a password: ")
    if password in user:
        return "Logged in successfully"
    else:
        return "Logged in failed!!!"


print(login())

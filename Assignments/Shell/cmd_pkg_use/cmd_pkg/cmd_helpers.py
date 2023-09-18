import os
import pwd

def get_username_from_uid(uid):
    try:
        user_info = pwd.getpwuid(uid)
        return user_info.pw_name
    except KeyError:
        return None  # User not found

# Replace 'uid' with the user ID for which you want to get the username
uid = 1  # Replace with the actual UID
username = get_username_from_uid(uid)

# if username:
#     print(f"Username for UID {uid}: {username}")
# else:
#     print(f"No username found for UID {uid}")

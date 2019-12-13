from GLOBAL import GLOBAL_DATA 

def auth_password_reset(reset_code, new_password):
    global GLOBAL_DATA

    valid_reset_code = False
    for users in GLOBAL_DATA["users"]:
        if reset_code == users.reset_code:
            valid_reset_code = True
            break
    
    if valid_reset_code == False:
        raise ValueError

    if len(new_password) < 6:
        raise ValueError

    users.add_crypted_password(new_password)
    return {}
    
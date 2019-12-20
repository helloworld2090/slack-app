from GLOBAL import (GLOBAL_DATA , User, Channel, generate_token, 
generate_user_id, get_user_from_token, get_user_from_u_id, Message,
is_admin_or_owner_token, re_calibrate_msgID, get_u_id_from_token)
import re

def user_profile_setemail(token, email):
    global GLOBAL_DATA

    rgx = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if not re.search(rgx, email):
        raise ValueError

    for users in GLOBAL_DATA["users"]:
        if email == users.email:
            raise ValueError

    
    index = get_u_id_from_token(token)

    target_user = GLOBAL_DATA["users"][index]
    target_user.email = email
    return {}

if __name__ == "__main__":
    from auth_login import auth_login
    from auth_register import auth_register
    from user_profile import user_profile
    

    user = auth_register('valid_email@email.com', 'valid_password', 'valid_first', 'valid_last')
    res1 = auth_login('valid_email@email.com', 'valid_password')
    token1 = res1["token"]

    prev = user_profile(token1, 0)
    print(prev)
    user_profile_setemail(token1, "new_email@gmial.com")
    prev = user_profile(token1, 0)
    print(prev)
    print(GLOBAL_DATA["users"][0].email)

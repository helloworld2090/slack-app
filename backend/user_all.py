from GLOBAL import (GLOBAL_DATA , User, Channel, generate_token, 
generate_user_id, get_user_from_token, get_user_from_u_id, Message,
is_admin_or_owner_token, re_calibrate_msgID, get_u_id_from_token)

def user_all():
    user_lst = []
    for users in GLOBAL_DATA["users"]:
        user_lst.append(users.First_name)
    
    return {"users" : user_lst}


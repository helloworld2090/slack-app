from GLOBAL import (GLOBAL_DATA , User, Channel, generate_token, 
generate_user_id, get_user_from_token, get_user_from_u_id, Message,
is_admin_or_owner_token, re_calibrate_msgID, get_u_id_from_token)
import re

def user_profile_sethandle(token, handle_str):
    global GLOBAL_DATA

    # invalid handle length
    if len(handle_str) < 3  or 20 < len(handle_str):
        raise ValueError

    #if the handle is aldready being used
    for users in GLOBAL_DATA["users"]:
        if handle_str == users.handle_name:
            raise ValueError
    
    index = get_u_id_from_token(token)

    target_user = GLOBAL_DATA["users"][index]
    target_user.handle_name = handle_str
    return {}


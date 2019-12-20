from GLOBAL import (GLOBAL_DATA , User, Channel, generate_token, 
generate_user_id, get_user_from_token, get_user_from_u_id, Message,
is_admin_or_owner_token, re_calibrate_msgID, get_u_id_from_token)

def user_profile(token, u_id):
    if u_id < 0 or u_id >= len(GLOBAL_DATA["users"]):
        raise ValueError
    
    target_user = GLOBAL_DATA["users"][u_id]

    return {"email": target_user.email, "first name" : target_user.First_name,
    "last name": target_user.Lastname, "handle": target_user.handle}
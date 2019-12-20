from GLOBAL import (GLOBAL_DATA , User, Channel, generate_token, 
generate_user_id, get_user_from_token, get_user_from_u_id, Message,
is_admin_or_owner_token, re_calibrate_msgID, get_u_id_from_token)

def user_profile_setname(token, name_first, name_last):
    
    for names in [name_first, name_last]:
        if 0 >= len(names) or len(names) > 50:
            raise ValueError

    non_punc_list = ["." , "," , "!", ";", ":", "?"]
    if name_first[0] in non_punc_list:
        raise ValueError

    global GLOBAL_DATA
    index = get_u_id_from_token(token)

    target_user = GLOBAL_DATA["users"][index]
    target_user.First_name = name_first
    target_user.Lastname = name_last
    return {}


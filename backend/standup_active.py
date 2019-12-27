from GLOBAL import (GLOBAL_DATA , User, Channel, generate_token, 
generate_user_id, get_user_from_token, get_user_from_u_id, Message,
is_admin_or_owner_token, re_calibrate_msgID, get_u_id_from_token)

from time import time

def standup_start(token, channel_id, length):
    global GLOBAL_DATA

    if channel_id < 0 or channel_id >= len(GLOBAL_DATA["channels"]):
        raise ValueError

    standup_dict = {}
    now = time.time()
    future = now + length
    
    target_channel = GLOBAL_DATA["channels"][channel_id]
    target_channel.standup_active = True
    while time.time() < future:
        pass
    
    target_channel.standup_active = False 
    GLOBAL_DATA["messages"].append(standup_dict)    

    return {"time finish" : future}



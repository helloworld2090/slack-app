from GLOBAL import (GLOBAL_DATA, standup_lst, User, Channel, generate_token, 
generate_user_id, get_user_from_token, get_user_from_u_id, Message,
is_admin_or_owner_token, re_calibrate_msgID, owner_of_these_channels)
from Error import AccessError

from standup_start import standup_start

def standup_send(token, channel_id, message):
    global GLOBAL_DATA
    global standup_lst
    if channel_id < 0 or channel_id >= len(GLOBAL_DATA["channels"]):
        raise ValueError
        
    if len(message) > 1000:
        raise ValueError

    target_channel = GLOBAL_DATA["channels"][channel_id]
    user = get_user_from_token(token)
    if user not in target_channel.members:
        raise AccessError
    
    if target_channel.standup_active == False:
        raise ValueError
    
    # all errors passed, then append to standup_send
    new_msg = {user : "message"}
    standup_lst.append(new_msg)
    return {}

    
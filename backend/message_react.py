from GLOBAL import (GLOBAL_DATA , User, Channel, generate_token, 
generate_user_id, get_user_from_token, get_user_from_u_id, Message,
is_admin_or_owner_token, re_calibrate_msgID, get_u_id_from_token)

from Error import AccessError

def message_react(token, message_id, react_id):
    global GLOBAL_DATA

    #invalid message_id
    if message_id < 0 or message_id >= len(GLOBAL_DATA["messages"]):
        raise ValueError

    # invalid react
    if react_id != 1:
        raise ValueError
    
    target_msg = GLOBAL_DATA["messages"][message_id]
    # message already reacted
    if target_msg.react_id == 1:
        raise ValueError
    
    target_msg.react_id = 1
    return {}


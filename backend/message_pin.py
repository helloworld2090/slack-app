from GLOBAL import (GLOBAL_DATA , User, Channel, generate_token, 
generate_user_id, get_user_from_token, get_user_from_u_id, Message,
is_admin_or_owner_token, re_calibrate_msgID, get_u_id_from_token)

from Error import AccessError

def message_pin(token, message_id):
    global GLOBAL_DATA
    # testing
    #invalid message_id
    if message_id < 0 or message_id >= len(GLOBAL_DATA["messages"]):
        raise ValueError

    # token is not admin
    if is_admin_or_owner_token(token) == False:
        raise ValueError
    
    target_msg = GLOBAL_DATA["messages"][message_id]
   
    # message already pinned
    if target_msg.is_pinned == True:
        raise ValueError
    
    for Channels in GLOBAL_DATA["channels"]:
        for msgs in Channels.messages:
            if message_id == msgs.message_id:
                break
    
    if get_user_from_token(token) in Channels.members:
        target_msg.is_pinned = True
        return {}

    else:
        raise AccessError


from GLOBAL import (GLOBAL_DATA , User, Channel, generate_token, 
generate_user_id, get_user_from_token, get_user_from_u_id, Message,
is_admin_or_owner_token, re_calibrate_msgID, get_u_id_from_token)

from Error import AccessError

def message_edit(token, message_id, message):
    global GLOBAL_DATA

    target_msg = GLOBAL_DATA["messages"][message_id]

    if target_msg.u_id != get_u_id_from_token(token) and is_admin_or_owner_token(token) == False:
        raise AccessError

    target_msg.message = list(message)
    return {}
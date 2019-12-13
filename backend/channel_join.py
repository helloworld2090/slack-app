from GLOBAL import (GLOBAL_DATA , User, Channel,generate_token, 
generate_user_id, get_user_from_token)
from Error import AccessError

def channel_join(token, Channel_id):
    global GLOBAL_DATA
    no_of_channels = len(GLOBAL_DATA["channels"]) 
    # invalid channel_id
    if Channel_id > no_of_channels - 1 or Channel_id < 0:
        raise ValueError
    
    for channels in GLOBAL_DATA["channels"]:
        if Channel_id == channels.id:
            if channels.is_public == False:
                raise AccessError
            else:
                user = get_user_from_token(token)
                channels.members.append(user)
                return {}

    
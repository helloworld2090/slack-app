from GLOBAL import (GLOBAL_DATA , User, Channel,generate_token, 
generate_user_id, get_user_from_token)
from Error import AccessError

def channel_leave(token, Channel_id):
    global GLOBAL_DATA
    user = get_user_from_token(token)
    print(user)
    
    no_of_channels = len(GLOBAL_DATA["channels"]) 
    if Channel_id > no_of_channels - 1 or Channel_id < 0:
        raise ValueError

    for channels in GLOBAL_DATA["channels"]:
        if Channel_id == channels.id:
            if user in channels.members:
                channels.members.remove(user)
                return {}
            else:
                raise AccessError 
                
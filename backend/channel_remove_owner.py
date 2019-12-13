from GLOBAL import (GLOBAL_DATA , User, Channel,generate_token, 
generate_user_id, get_user_from_token, get_user_from_u_id)
from Error import AccessError

def channel_remove_owner(token, channel_id, u_id):
    global GLOBAL_DATA
    no_of_channels = len(GLOBAL_DATA["channels"]) 
    # invalid channel_id
    if channel_id > no_of_channels - 1 or channel_id < 0:
        raise ValueError

    #when token : user us not an admin 
    owner_token = False
    for user in GLOBAL_DATA['users']:
        if user.token == token:
            if user.handle == 3:
                break
            else:
                raise AccessError
    
    name = get_user_from_u_id(u_id)
    target_channel = GLOBAL_DATA['channels'][channel_id]

    if name in target_channel.owners:
        target_channel.owners.remove(name)
        return {}
    else:
        raise ValueError
    



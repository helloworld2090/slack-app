from GLOBAL import (GLOBAL_DATA , User, Channel,generate_token, 
generate_user_id, get_user_from_token, get_user_from_u_id)
from Error import AccessError

def channel_addowner(token, Channel_id, u_id):
    global GLOBAL_DATA
    no_of_channels = len(GLOBAL_DATA["channels"]) 
    # invalid channel_id
    if Channel_id > no_of_channels - 1 or Channel_id < 0:
        raise ValueError

    owner_token = False

    for user in GLOBAL_DATA['users']:
        if user.token == token:
            if user.handle == 3:
                break
            else:
                raise AccessError

    name = get_user_from_u_id(u_id)
    target_channel = GLOBAL_DATA['channels'][Channel_id]

    if name not in target_channel.owners:
        target_channel.owners.append(name)
        return {}
    else:
        raise ValueError
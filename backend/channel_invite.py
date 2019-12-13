from GLOBAL import (GLOBAL_DATA , User, Channel,generate_token, 
generate_user_id, get_user_from_token, get_user_from_u_id, check_valid_uid,
get_channel_from_ch_id)
from Error import AccessError

def channel_invite(token, Channel_id, u_id):
    global GLOBAL_DATA
    no_of_channels = len(GLOBAL_DATA["channels"]) 
    # invalid channel_id
    if Channel_id > no_of_channels - 1 or Channel_id < 0:
        raise ValueError

    # invalid u id
    if check_valid_uid(u_id) == False:
        raise ValueError

    name = get_user_from_u_id(u_id)
    target_ch = get_channel_from_ch_id(Channel_id)

    if name in target_ch.members:
        #if user is already a member
        raise AccessError
    else:
        target_ch.members.append(name)
        return {}



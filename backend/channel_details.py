from GLOBAL import (GLOBAL_DATA , User, Channel, generate_token, 
generate_user_id, get_user_from_token, get_user_from_u_id)
from Error import AccessError

def channel_details(token, channel_id):
    global GLOBAL_DATA
    no_of_channels = len(GLOBAL_DATA["channels"]) 
    # invalid channel_id
    if channel_id > no_of_channels - 1 or channel_id < 0:
        raise ValueError

    #when the user is not part of the channel
    user_is_member = False
    name = get_user_from_token(token)
    target_channel = GLOBAL_DATA["channels"][channel_id]

    if name not in target_channel.members:
        raise AccessError

    return {"name" : target_channel.name, "owner_members": target_channel.owners, "all_members": target_channel.members}

if __name__ == "__main__":
    from auth_login import auth_login
    from auth_register import auth_register
    from channel_invite import channel_invite
    from channel_create import channel_create
    from Error import AccessError

    user1 = auth_register('valid_email1@email.com', 'valid_password1', 'valid_first1', 'valid_last1')
    res1 = auth_login('valid_email1@email.com', 'valid_password1')
    token1 = res1['token']
    u_id1 = res1['u_id']
    channel_id1 = channel_create(token1, 'Example channel 1', True)['channel_id']
    t = channel_details(token1, channel_id1)
    print(t)

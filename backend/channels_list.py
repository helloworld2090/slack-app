from GLOBAL import (GLOBAL_DATA , User, Channel, generate_token, 
generate_user_id, get_user_from_token, get_user_from_u_id)

def channels_list(token):
    name = get_user_from_token(token)
    print(name)
    channel_list = []

    for channels in GLOBAL_DATA["channels"]:
        new_dict = {}
        if name in channels.members:
            new_dict["id"] = channels.id
            new_dict["name"] = channels.name
            #print(new_dict)
            channel_list.append(new_dict)
    
    
    return {"channels" : channel_list}

if __name__ == "__main__":

    from auth_login import auth_login
    from auth_register import auth_register
    from channel_invite import channel_invite
    from channel_create import channel_create
    from channels_list import channels_list

    user1 = auth_register('valid_email1@email.com', 'valid_password1', 'valid_first1', 'valid_last1')
    res1 = auth_login('valid_email1@email.com', 'valid_password1')
    token1 = res1['token']
    u_id1 = res1['u_id']
    n_ch = channel_create(token1, 'Example channel 1', True)

    t = channels_list(token1)
    print(t)
from GLOBAL import (GLOBAL_DATA , User, Channel, generate_token, 
generate_user_id, get_user_from_token, get_user_from_u_id)
from Error import AccessError

def channel_messages(token, channel_id, start):
    global GLOBAL_DATA
  
    # invalid channel_id
    no_of_channels = len(GLOBAL_DATA["channels"]) 
    if channel_id > no_of_channels - 1 or channel_id < 0:
        raise ValueError

    #when the user is not part of the channel
    user_is_member = False
    name = get_user_from_token(token)
    target_channel = GLOBAL_DATA["channels"][channel_id]
    if name not in target_channel.members:
        raise AccessError
    
    target_channel.messages = [f"message{i}" for i in range(0,20)]

    #invalid when start is greater than the length of messages
    if start > len(target_channel.messages):
        raise ValueError
    
    msg_lst = []
    LENGTH_OF_MESSAGES = len(target_channel.messages)
    if LENGTH_OF_MESSAGES > 50:
        for i in range(0,50):
            i += start
            msg_lst.append(target_channel.messages[i])
        last = start + 50

    else:  
        print("case 2")

        for i in range (0, LENGTH_OF_MESSAGES):
            i += start
            msg_lst.append(target_channel.messages[i])    
        last = -1 

    return {"messages": msg_lst, "start": start, "end": last}

if __name__ =="__main__":
    import pytest

    from auth_login import auth_login
    from auth_register import auth_register
    from channel_create import channel_create
    from Error import AccessError
    #from message_send import message_send

    # Create channel owner
    user1 = auth_register('valid_email1@email.com', 'valid_password1', 'valid_first1', 'valid_last1')
    res1 = auth_login('valid_email1@email.com', 'valid_password1')
    u_id1 = res1['u_id']
    token1 = res1['token']
    channel_id1 = channel_create(token1, 'Example channel 1', True)['channel_id']
    t =channel_messages(token1, channel_id1, 10)
    print(t) 
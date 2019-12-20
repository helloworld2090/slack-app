from GLOBAL import (GLOBAL_DATA , User, Channel, generate_token, 
generate_user_id, get_user_from_token, get_user_from_u_id, Message)
from time import time
from Error import AccessError
from message_send import message_send                     

def message_send(token, channel_id, message, time_sent):
    global GLOBAL_DATA                                                                                                                                           
    # Send message from authorised user to channel
                                                    
    if len(message) > 1000:                                 
        raise ValueError("Message is more than 1000 characters")
    elif time_sent < 0:
        raise ValueError
    elif channel_id < 0 or len(GLOBAL_DATA["channels"]) <= channel_id:
        raise ValueError

    # raise AccessError when user has has not joined the channel                                    
    target_channel = GLOBAL_DATA["channels"][channel_id]
    user_name = get_user_from_token(token)
    if user_name not in target_channel.members:
        raise AccessError("authorised user has not joined the channel they are trying to post to")

    #timer start
    now = time.time()
    future = now + time_sent
    while time.time() < future:
        pass
        
    new_message = Message(token, message)
    target_channel.messages.append(new_message)
    
    GLOBAL_DATA["messages"].append(new_message)

    return {"message_id": new_message.message_id}


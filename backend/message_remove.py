from GLOBAL import (GLOBAL_DATA , User, Channel, generate_token, 
generate_user_id, get_user_from_token, get_user_from_u_id, Message,
is_admin_or_owner_token, re_calibrate_msgID)

from Error import AccessError

def message_remove(token, message_id):

    global GLOBAL_DATA
    # when the token is not admin or owner of the channel 
    if is_admin_or_owner_token(token) == False:
        raise AccessError
    # looping over channels and message ids


    #message ID is not a validn m id
    if message_id >= len(GLOBAL_DATA["messages"]):
        raise ValueError("Message (based on ID) no longer exists")

    #removing the message
    remove_msg(message_id)

    return {}

def remove_msg(message_id):
    # need to remove from global data and the channel attribute
    global GLOBAL_DATA

    # removed from global data
    for msg in GLOBAL_DATA["messages"]:
        if msg.message_id == message_id:
            target_msg = msg
            break
    GLOBAL_DATA["messages"].remove(target_msg)

    # remove from channel attribute
    for channels in GLOBAL_DATA["channels"]:
        for messages in channels.messages:
            if messages.message_id == message_id:
      
                channels.messages.remove(target_msg)
    
    re_calibrate_msgID()
    return 0
    
if __name__ == "__main__":
    from auth_login import auth_login
    from auth_register import auth_register
    from channel_create import channel_create
    from Error import AccessError
    from message_send import message_send
    user1 = auth_register("valid_email1@email.com", "valid_password1", "valid_first1", "valid_last1")
    res1 = auth_login("valid_email1@email.com", "valid_password1")
    token1 = res1["token"]
    channel_id1 = channel_create(token1, "Example channel 1", True)["channel_id"]

    message_send(token1, channel_id1, "test_message1") # assume message id 0
    message_send(token1, channel_id1, "test_message2") # assume message id 1
    message_send(token1, channel_id1, "test_message3") # assume message id 2
    message_send(token1, channel_id1, "test_message3") # assume message id 2
    message_send(token1, channel_id1, "test_message3") # assume message id 2

    #message_remove(token1, 1) 

    print(GLOBAL_DATA["messages"][0].message_id)
    print(GLOBAL_DATA["messages"][1].message_id)
    print(GLOBAL_DATA["messages"][2].message_id)
    print(GLOBAL_DATA["messages"][3].message_id)
    print(GLOBAL_DATA["messages"][4].message_id)

    message_remove(token1, 1)
    message_remove(token1, 1)
    message_remove(token1, 1)

    print("renewed")
    print(GLOBAL_DATA["messages"][0].message_id)
    print(GLOBAL_DATA["messages"][1].message_id)






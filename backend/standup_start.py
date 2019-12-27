from GLOBAL import (GLOBAL_DATA , standup_lst, User, Channel, generate_token, 
generate_user_id, get_user_from_token, get_user_from_u_id, Message,
is_admin_or_owner_token, re_calibrate_msgID, get_u_id_from_token)
from datetime import datetime
import time
from timer import timer_countdown

def standup_start(token, channel_id, length):
    global GLOBAL_DATA
    global standup_lst
    if channel_id < 0 or channel_id >= len(GLOBAL_DATA["channels"]):
        raise ValueError

    #standup_lst = {}
    #now = time.time()
    future = time.time() + length
    
    
    #timer_start()
    while time.time() < future:
        timer_countdown(time.time(), future, channel_id)
    
    
    target_channel.standup_active = False 
    target_channel.messages.append(standup_lst)  
    GLOBAL_DATA["messages"].append(standup_lst)     

    return {"time finish" : datetime.now()}



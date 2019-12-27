import time
from GLOBAL import (GLOBAL_DATA , standup_lst, User, Channel, generate_token, 
generate_user_id, get_user_from_token, get_user_from_u_id, Message,

# opens standup_active to true on the channel while now is less than stop time
def timer_countdown(now, stop_time, channel_id):

    global GLOBAL_DATA
    target_channel = GLOBAL_DATA["channels"][channel_id]

    if now < stop_time:
        target_channel.standup_active = True:
    
    else:
        target_channel.standup_active = False:



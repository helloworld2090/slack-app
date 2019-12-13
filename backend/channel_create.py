from GLOBAL import (GLOBAL_DATA , User, Channel,generate_token, 
generate_user_id)

def channel_create(token, name, is_public):
    global GLOBAL_DATA
    if len(name) > 20:
        raise ValueError

    new_channel = Channel(token, name, is_public)
    new_channel.add_channel_id()
    GLOBAL_DATA["channels"].append(new_channel)
    return {"channel_id" : new_channel.id}


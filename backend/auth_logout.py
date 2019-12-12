from GLOBAL import GLOBAL_DATA , User, generate_token, generate_user_id

def auth_logout(token):
    global GLOBAL_DATA
    online_user = False
    #print(GLOBAL_DATA["active_tokens"])
    #print("====")
    #print(type(GLOBAL_DATA["active_tokens"]))

    if token in GLOBAL_DATA["active_tokens"]:
        online_user = True
    
    if online_user == True:
        GLOBAL_DATA["active_tokens"].remove(token)
        return {"is_success": True}

    else:
        return {"is_success" : False}


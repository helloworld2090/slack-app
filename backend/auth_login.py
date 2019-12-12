import jwt
import hashlib
import re
from GLOBAL import GLOBAL_DATA , User, generate_token, generate_user_id

def auth_login(email, password):
    global GLOBAL_DATA
    #invalid email
    rgx = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if not (re.search(rgx, email)):
        raise ValueError
    
    #email does nto exists
    user_authenticated = False
    for users in GLOBAL_DATA["users"]:
        if users.email == email and users.password == hashlib.sha256(password.encode()).hexdigest():
            user_authenticated = True
            break
    
    if user_authenticated == True:
        if users.token not in GLOBAL_DATA["active_tokens"]:
            GLOBAL_DATA["active_tokens"].append(users.token)
            
        return {"u_id" : users.u_id, "token" : users.token}
    else:
        raise ValueError("email or password incorrect")

    


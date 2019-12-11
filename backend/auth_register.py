import jwt
import re

from GLOBAL import GLOBAL_DATA , User, generate_token, generate_user_id

def auth_register(email, password, name_first, name_last):
    global GLOBAL_DATA
    #passwords are incorrect if less than 4 chars
    if len(password) < 6:
        raise ValueError
    
    # invalid email    
    #if another user has the email
    for user in GLOBAL_DATA["users"]:
        if user.email == email:
            raise ValueError("email already exists")
    
    #if name_first or name_last is out of bounds
    if len(name_first) < 1 or len(name_first) > 50:
        raise ValueError

    if len(name_last) < 1 or len(name_last) > 50:
        raise ValueError
    
    rgx = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    if(re.search(rgx, email)) :
        new_user = User(email, name_first, name_last)
        new_user.add_crypted_password(password)

        token = generate_token(new_user, email)
        u_id = generate_user_id(new_user)
        GLOBAL_DATA["users"].append(new_user)

    elif not (re.search(rgx, email)):
        raise ValueError("email not valid")
    print(GLOBAL_DATA)
    """
    attrs = vars(new_user)
    print(', '.join("%s: %s" % item for item in attrs.items())) """


    return {"u_id": u_id, "token": token}
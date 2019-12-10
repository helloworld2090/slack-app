import jwt
import re
from GLOBAL.py import GLOBAL_DATA, User

def auth_login(email, password):
    #passwords are incorrect if less than 4 chars
    if len(password) <= 4:
        raise ValueError
    
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if re.search(regex, email) == True:
        User(email, )
    


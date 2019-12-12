import hashlib
import jwt
import datetime

GLOBAL_DATA = {
    "users" : [],
    "active_tokens": [],
    "channels" : []
}

secret = 'senpai'

class User:
    def __init__(self, email, First_name, Lastname):
        self.email = email
        self.First_name = First_name
        self.Lastname = Lastname
        self.token = 0
        self.u_id = 0 

    def add_crypted_password(self, password):
        self.password = hashlib.sha256(password.encode()).hexdigest() 

    
def generate_token(user, email):                                            
    encoded_jwt = jwt.encode({'token': email}, secret, algorithm = 'HS256')
    user.token = encoded_jwt  
    global GLOBAL_DATA
    GLOBAL_DATA["active_tokens"].append(encoded_jwt)                      
    return encoded_jwt                              

def generate_user_id(user):
    # only takes in a user class as parameter
    no_of_users = len(GLOBAL_DATA["users"])
    user.u_id = no_of_users
    return no_of_users


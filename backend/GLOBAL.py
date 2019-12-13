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
        # 3: owner
        # 2: admin
        # 1: member
        self.handle = generate_handle()
        

    def add_crypted_password(self, password):
        self.password = hashlib.sha256(password.encode()).hexdigest() 

    def add_reset_code(self,user_email):
        self.reset_code = hashlib.sha256(user_email.encode()).hexdigest()

class Channel():
    def __init__ (self, token, name, is_public):
        self.name = name
        self.is_public = is_public
        self.messages = []
        self.members = [get_user_from_token(token)]
        #add channel_id
        # owners by email
        self.owners = get_user_from_token(token)
        
    def add_channel_id(self):
        channel_no = 0
        for channels in GLOBAL_DATA["channels"]:
            channel_no += 1
        self.id = channel_no

def generate_handle():
    if len(GLOBAL_DATA["users"]) == 0:
        return 3
    else:
        return 1

def generate_token(user, email):                                            
    encoded_jwt = jwt.encode({'token': email}, secret, algorithm = 'HS256')
    user.token = encoded_jwt  
    global GLOBAL_DATA
    GLOBAL_DATA["active_tokens"].append(encoded_jwt)
    #print(encoded_jwt)                      
    return encoded_jwt                              

def generate_user_id(user):
    # only takes in a user class as parameter
    no_of_users = len(GLOBAL_DATA["users"])
    user.u_id = no_of_users
    return no_of_users

def get_user_from_token(token): 
    decoded = jwt.decode(token, secret, algorithms = ['HS256'])
    decoded_email = decoded['token']
    #print(decoded_email)
    for users in GLOBAL_DATA["users"]:
        if users.email == decoded_email:
            #print("ture")
            return users.First_name

# given u_id as input - return the first name of the u_id
def get_user_from_u_id(u_id): 
    for users in GLOBAL_DATA["users"]:
        if users.u_id == u_id:
            return users.First_name

# given u_id as input - checks if the u_id is valid in the system
def check_valid_uid(u_id):
    if 0 <= u_id and u_id < len(GLOBAL_DATA["users"]):
        return True
    else:
        return False 

def get_channel_from_ch_id(c_id): 
    for channels in GLOBAL_DATA["channels"]:
        if c_id == channels.id:
            return channels

def clear_all():
    pass
    
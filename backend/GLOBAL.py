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
        """
        self.handle = 0 : refers to admin previledges
        """

    def add_crypted_password(self, password):
        self.password = hashlib.sha256(password.encode()).hexdigest() 

    def add_reset_code(self,user_email):
        self.reset_code = hashlib.sha256(user_email.encode()).hexdigest()

 
class Channel():
    def __init__ (self, token, name, is_public):
        self.name = name
        self.is_public = is_public
        self.messages = []
        self.members = [name]
        #add channel_id
        # owners by email
        self.owners = [name]
        
    def add_channel_id(self):
        channel_no = 0
        for channels in GLOBAL_DATA["channels"]:
            channel_no += 1
        self.id = channel_no


def generate_token(user, email):                                            
    encoded_jwt = jwt.encode({'token': email}, secret, algorithm = 'HS256')
    user.token = encoded_jwt  
    global GLOBAL_DATA
    GLOBAL_DATA["active_tokens"].append(encoded_jwt)
    print(encoded_jwt)                      
    return encoded_jwt                              

def generate_user_id(user):
    # only takes in a user class as parameter
    no_of_users = len(GLOBAL_DATA["users"])
    user.u_id = no_of_users
    return no_of_users

def get_user_from_token(token): 
    decoded = jwt.decode(token, secret, algorithms = ['HS256'])
    decoded_email = decoded['token']

    username = ""
    for users in GLOBAL_DATA['users']:
        if decoded_email == users.email:
            username = users.First_name
            break

    return username



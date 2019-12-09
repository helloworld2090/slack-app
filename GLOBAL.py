import hashlib

from jwt import PyJWT
import datetime


class User:
    def __init__(self, firstName, lastName, email, password, handle, u_id):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.handle = handle
        self.u_id = u_id

class PasswordReset:
    def __init__(self, email, resetCode):
        self.email = email
        self.resetCode = resetCode

class Channel:
    def __init__(self, name, channel_id, is_public, owner):
        self.name = name
        self.channel_id = channel_id
        self.is_public = is_public
        self.owners = [owner]
        self.members = [owner] # assume the person creating the channels is automatically a member
        self.messages = []
        self.message_id = []
        self.react_id = []
        self.message_pinned = []
        self.standup = None
        self.standupMsgs = None
        

    def getOwners(self):
        return self.owners

data = {
    'users': [],
    'validTokens': [],
    'passwordResets': [],
    'channels' : [],
}

SECRET = 'abc'
jwt = PyJWT()

def generateToken(email):
    #global SECRET
    global jwt
    encoded = jwt.encode({'email': email}, SECRET, algorithm='HS256')
    return str(encoded)

def getUserFromToken(token):
    #jwt = PyJWT()
    #global SECRET
    global jwt
    print(token)
    token = token[2:-1]
    print(token)
    decoded = jwt.decode(token.encode(), SECRET, algorithm='HS256')
    return decoded['email']

def getUIDFromEmail(email):
    for i in data['users']:
        if i.email == email:
            return i.u_id

def hashPassword(password):
    return hashlib.sha256(password.encode()).hexdigest()


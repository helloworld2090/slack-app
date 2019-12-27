import re
import sys
from json import dumps

from flask import Flask, request
from flask_cors import CORS
from jwt import PyJWT

#from backend.data import SECRET
import backend.GLOBAL
from backend.auth_login import auth_login
from backend.auth_logout import auth_logout
from backend.auth_passwordreset_request import auth_passwordreset_request
from backend.auth_passwordreset_reset import auth_passwordreset_reset
from backend.auth_register import auth_register

from backend.channel_addowner import channel_addowner
from backend.channel_details import channel_details
from backend.channel_invite import channel_invite
from backend.channel_leave import channel_leave
from backend.channel_removeowner import channel_removeowner
from backend.channel_create import channel_create
from backend.channels_list import channels_list
from backend.channels_listall import channels_listall
from backend.channel_join import channel_join

from backend.message_sendlater import message_sendlater
from backend.message_send import message_send
from backend.message_remove import message_remove
from backend.message_edit import message_edit
from backend.message_react import message_react
from backend.message_unreact import message_unreact
from backend.message_pin import message_pin
from backend.message_unpin import message_unpin

from backend.user_profile import user_profile
from backend.user_profile_setname import user_profile_setname
from backend.user_profile_setemail import user_profile_setemail
from backend.user_profile_sethandle import user_profile_sethandle
from backend.user_profiles_uploadphoto import user_profiles_uploadphoto

from backend.users_all import users_all
"""
from backend.standup_start import standup_start
from backend.standup_active import standup_active
from backend.standup_send import standup_send

from backend.search import search

from backend.admin_userpermission_change import admin_userpermission_change

from flask_mail import Mail, Message

#from auth_login import auth_login """


APP = Flask(__name__)
CORS(APP)

APP.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'ethicalpythonlads@gmail.com',
    MAIL_PASSWORD = 'ethicalpython',
)

jwt = PyJWT()

global SECRET

@APP.route("/auth/login", methods = ['POST'])
def login():
    """ Log in user given email and password """
    email = request.form.get('email')
    password = request.form.get('password')
    
    return dumps(auth_login(email, password))

@APP.route('/auth/register', methods=['POST'])
def register():
    """ Register user given email, password, firstname and lastname """
    firstName = request.form.get('name_first')
    lastName = request.form.get('name_last')
    email = request.form.get('email')
    password = request.form.get('password')

    return dumps(auth_register(email, password, firstName, lastName))

@APP.route('/auth/logout', methods=['POST'])
def logout():
    """ Logout logged-in user """
    token = request.form.get('token')

    return dumps(auth_logout(token))

@APP.route('/auth/passwordreset/request', methods=['POST'])
def passwordreset_request():
    """ Request password reset """
    email = request.form.get('email')
    
    resetRequest = auth_passwordreset_request(email)

    if resetRequest['validEmail']:
        mail = Mail(APP)
        try:
            msg = Message('Password Reset Code',
                sender = 'ethicalpythonlads@gmail.com',
                recipients = [email])
            msg.body = 'Reset code: ' + resetRequest['resetCode']
            mail.send(msg)
        except Exception as e:
            print(str(e))

    return dumps({})


@APP.route('/auth/passwordreset/reset', methods=['POST'])
def passwordreset_reset():
    """ Reset password given valid reset code """
    resetCode = request.form.get('reset_code')
    newPassword = request.form.get('new_password')

    return dumps(auth_passwordreset_reset(resetCode, newPassword))

@APP.route('/channels/create', methods=['POST'])
def create():
    """ Create channel """
    token = request.form.get('token')
    name = request.form.get('name')
    is_public = request.form.get('is_public')

    return dumps(channel_create(token, name, is_public))

# Leave until channel_create fixed

@APP.route('/channels/list', methods=['GET'])
def list1():
    """ List channels user is a member of """
    token = request.args.get('token')

    return dumps(channels_list(token))

@APP.route('/channels/listall', methods=['GET'])
def listall():
    """ List all channels """
    token = request.args.get('token')

    return dumps(channels_listall(token))

@APP.route('/channel/invite', methods=['POST'])
def invite():
    """ Invite user to join a channel """
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    u_id = request.form.get('u_id')

    return dumps(channel_invite(token, channel_id, u_id))

@APP.route('/channel/details', methods=['GET'])
def details():
    """ Get channel details """
    token = request.args.get('token')
    channel_id = request.args.get('channel_id')

    return dumps(channel_details(token, channel_id))

@APP.route('/channel/leave', methods=['POST'])
def leave():
    """ Leave channel """
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')

    return dumps(channel_leave(token, channel_id))

@APP.route('/channel/join', methods=['POST'])
def join():
    """ Leave channel """
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')

    return dumps(channel_join(token, channel_id))

@APP.route('/channel/addowner', methods=['POST'])
def addOwner():
    """ Make user an owner of the channel """
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    u_id = request.form.get('u_id')

    return dumps(channel_addowner(token, channel_id, u_id))

@APP.route('/channel/removeowner', methods=['POST'])
def removeOwner():
    """ Remove user as an owner of the channel """
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    u_id = request.form.get('u_id')

    return dumps(channel_removeowner(token, channel_id, u_id))
    

@APP.route('/message/sendlater', methods = ['POST']) 
def sendLater():
    """ send a message at a specified future time """
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    time_sent = request.form.get('time_sent')    
    message = request.form.get('message')
    
    return dumps(message_sendlater(token, channel_id, message, time_sent))

@APP.route('/message/send', methods = ['POST']) 
def send():
    """ send a message """
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    message = request.form.get('message')    
    
    return dumps(message_send(token, channel_id, message))

@APP.route('/message/remove', methods = ['DELETE']) 
def removeMessage():
    """ remove a message """
    token = request.form.get('token')
    message_id = request.form.get('message_id')    
    
    return dumps(message_remove(token, message_id))

@APP.route('/message/edit', methods = ['PUT']) 
def editMessage():
    """ edit a message """
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    message = request.form.get('message')    
    
    return dumps(message_edit(token, message_id, message))

@APP.route('/message/react', methods = ['POST']) 
def reactMessage():
    """ react to a message """
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    react_id = request.form.get('react_id')    
    
    return dumps(message_react(token, message_id, react_id))

@APP.route('/message/unreact', methods = ['POST']) 
def unreactMessage():
    """ unreact to a message """
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    react_id = request.form.get('react_id')    
    
    return dumps(message_unreact(token, message_id, react_id))

@APP.route('/message/pin', methods = ['POST']) 
def pinMessage():
    """ pin a message """
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    
    return dumps(message_pin(token, message_id))

@APP.route('/message/unpin', methods = ['POST']) 
def unpinMessage():
    """ unpin a message """
    token = request.form.get('token')
    message_id = request.form.get('message_id')
    
    return dumps(message_unpin(token, message_id))

@APP.route('/user/profile', methods = ['GET']) 
def userProfile():
    """ get user profile """
    token = request.args.get('token')
    u_id = request.args.get('u_id')
    
    return dumps(user_profile(token, u_id))

@APP.route('/user/profile/setname', methods = ['PUT']) 
def profileSetName():
    """ set user's name"""
    token = request.form.get('token')
    name_first = request.form.get('name_first')
    name_last = request.form.get('name_last')    
    
    return dumps(user_profile_setname(token, name_first, name_last))

@APP.route('/user/profile/setemail', methods = ['POST']) 
def userEmail():
    """ set user's email """
    token = request.form.get('token')
    email = request.form.get('email') 
    
    return dumps(user_profile_setemail(token, email))

@APP.route('/user/profiles/sethandle', methods = ['PUT']) 
def setHandle():
    """ react to a message """
    token = request.form.get('token')
    handle_str = request.form.get('handle_str')
    
    return dumps(user_profile_sethandle(token, handle_str))

@APP.route('/user/profiles/uploadphoto', methods = ['POST']) 
def uploadPhoto():
    """ react to a message """
    token = request.form.get('token')
    img_url = request.form.get('img_url')
    x_start = request.form.get('x_start')
    y_start = request.form.get('y_start')
    x_end = request.form.get('x_end')
    y_end = request.form.get('y_end')
    
    return dumps(user_profiles_uploadphoto(token, img_url, x_start, y_start, x_end, y_end))
    
@APP.route('/users/all', methods = ['GET']) 
def usersAll():
    """ react to a message """
    token = request.args.get('token') 
    
    return dumps(users_all(token))

@APP.route('/standup/start', methods = ['POST']) 
def standupStart():
    """ react to a message """
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    length = request.form.get('length')    
    
    return dumps(message_react(token, channel_id, length))

@APP.route('/standup/active', methods = ['GET']) 
def standupActive():
    """ react to a message """
    token = request.args.get('token')
    channel_id = request.args.get('channel_id')
    
    return dumps(standup_active(token, channel_id))

@APP.route('/standup/send', methods = ['POST']) 
def standupSend():
    """ react to a message """
    token = request.form.get('token')
    channel_id = request.form.get('channel_id')
    message = request.form.get('message')    
    
    return dumps(standup_send(token, channel_id, message))

@APP.route('/search', methods = ['GET']) 
def searchFn():
    """ react to a message """
    token = request.args.get('token')
    query_str = request.form.get('query_str')
    
    return dumps(search(token, query_str))

@APP.route('/admin/userpermission/change', methods = ['POST']) 
def adminChange():
    """ react to a message """
    token = request.form.get('token')
    u_id = request.form.get('u_id')
    permission_id = request.form.get('permission_id')    
    
    return dumps(admin_userpermission_change(token, u_id, permission_id))


@APP.route('/echo/get', methods=['GET'])
def echo1():
    """ Description of function """
    return dumps({
        'echo' : request.args.get('echo'),
    })

@APP.route('/echo/post', methods=['POST'])
def echo2():
    """ Description of function """
    return dumps({      
        'echo' : request.form.get('echo'),
    })

if __name__ == '__main__':
    APP.run(port=(sys.argv[1] if len(sys.argv) > 1 else 5000), debug=True)

import pytest

from Error import AccessError
from user_profile_setname import user_profile_setname
from auth_login import auth_login
from auth_register import auth_register
from user_all import user_all
from standup_start import standup_start
from standup_send import standup_send
from channel_create import channel_create

user1 = auth_register('valid_email1@email.com', 'valid_password1', 'valid_first1', 'valid_last1')
res1 = auth_login('valid_email1@email.com', 'valid_password1')
token1 = res1['token']
u_id1 = res1['u_id']
channel_id1 = channel_create(token1, 'Example channel 1', True)['channel_id']


def test_standup_send_1():
    #testing valid case 
    standup_start(token1, channel_id1, 3)
    assert standup_send(token1, channel_id1 ,"test") == {}
    
    #testing invalid case
    #assert admin_userpermission_change("!", 135 , "eaifjij") == {}
"""
def test_standup_send_2():
    #ValueError exceptions Channel (based on ID) does not exist
    with pytest.raises(ValueError):
        standup_send("abcde", 0, "1"*1001)
                
def test_standup_send_3():    
    #ValueError exceptions Message is more than 1000 characters
    with pytest.raises(ValueError):
        standup_send("abcde", 135, "1001+ character string")
    
def test_standup_send_4():        
    #AccessError exceptions: authorised user is not an admin or owner
    with pytest.raises(AccessError):
        standup_send("abcde", 0, 0)
        
def test_standup_send_5():        
    #AccessError exceptions: authorised user is not an admin or owner
    with pytest.raises(AccessError):
        standup_send("abcde", 0, 0) """

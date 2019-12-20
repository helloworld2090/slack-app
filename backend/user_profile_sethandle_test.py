import pytest
from GLOBAL import (GLOBAL_DATA , User, Channel, generate_token, 
generate_user_id, get_user_from_token, get_user_from_u_id, Message,
is_admin_or_owner_token, re_calibrate_msgID, get_u_id_from_token)

from user_profile_sethandle import user_profile_sethandle
from auth_login import auth_login
from auth_register import auth_register


user = auth_register('valid_email@email.com', 'valid_password', 'valid_first', 'valid_last')
res2 = auth_login('valid_email@email.com', 'valid_password')
token1 = res2['token']
u_id = res2['u_id']


def test_user_profile_sethandle_1():
    #testing valid case
    assert GLOBAL_DATA["users"][0].handle_name == ""
    assert user_profile_sethandle(token1,"I"*20) == {}
    assert GLOBAL_DATA["users"][0].handle_name == "I"*20 

def test_user_profile_sethandle_another():
    #testing valid case
    assert user_profile_sethandle(token1,"asshole") == {}
    assert GLOBAL_DATA["users"][0].handle_name == "asshole" 

    
def test_user_profile_sethandle_2():
    #handle_str is no more than 20 characters
    with pytest.raises(ValueError):
        user_profile_sethandle(token1, "I"*21)
        

def test_user_profile_sethandle_sample():
    #handle_str is less than 3 chars
    with pytest.raises(ValueError):
        user_profile_sethandle(token1, "fe")


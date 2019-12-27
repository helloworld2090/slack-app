import pytest

from user_profile_setname import user_profile_setname
from auth_login import auth_login
from auth_register import auth_register
from user_all import user_all

def test_empty_user_base():
    assert user_all() == {"users" : []}

def test_userall_0():
    user = auth_register('valid_email@email.com', 'valid_password', 'valid_first', 'valid_last')
    res2 = auth_login('valid_email@email.com', 'valid_password')
    token = res2['token']
    u_id = res2['u_id']

    assert user_all() == {"users" : ["valid_first"]}

def test_userall_multiple():
    user_2 = auth_register('valid_email2@email.com', 'valid_password2', 'valid_first1', 'valid_last1')
    res2_2 = auth_login('valid_email2@email.com', 'valid_password2')
    
    user_3 = auth_register('valid_email3@email.com', 'valid_password3', 'valid_first2', 'valid_last2')
    res2_3 = auth_login('valid_email3@email.com', 'valid_password3')

    assert user_all() == {"users" : ["valid_first", "valid_first1", "valid_first2"]}

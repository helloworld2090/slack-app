import pytest

from user_profile_setname import user_profile_setname
from auth_login import auth_login
from auth_register import auth_register


user = auth_register('valid_email@email.com', 'valid_password', 'valid_first', 'valid_last')
res2 = auth_login('valid_email@email.com', 'valid_password')
token = res2['token']
u_id = res2['u_id']


def test_user_profile_setname_valid():
    #testing valid case
    assert user_profile_setname(token, "50 char string", "50 char string") == {}

def test_user_profile_setname_lenth1():
    #name_first is more than 50 characters
    with pytest.raises(ValueError):
        user_profile_setname(token, "I"*51, "50 char string")
        
def test_user_profile_setname_length2():    
    #name_last is more than 50 characters
    with pytest.raises(ValueError):
        user_profile_setname(token, "50 char string", "I"*51)

def test_user_profile_punctuation():
    #testing non-alphanumerical username
    with pytest.raises(ValueError):
        user_profile_setname(token, ".;,.", ".,,.")
    
def test_user_profile_noname():
    #testing noname
    with pytest.raises(ValueError):
        user_profile_setname(token, "", "Smith")



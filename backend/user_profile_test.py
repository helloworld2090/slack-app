import pytest

from user_profile import user_profile
from auth_login import auth_login
from auth_register import auth_register

user = auth_register('valid_email@email.com', 'valid_password', 'valid_first', 'valid_last')
res2 = auth_login('valid_email@email.com', 'valid_password')
token = res2['token']
u_id = res2['u_id']


def test_user_profile_valid():
    #testing valid case
    assert user_profile(token, 0) == {
    "email": 'valid_email@email.com', 
    "first name" : "valid_first",
    "last name": "valid_last", 
    "handle": 3
    }

def test_user_profile_identity1():
    #testing valid profile
    with pytest.raises(ValueError):
        assert user_profile(token, 2)

    
def test_user_profile_invalid():
    #User with u_id is not a valid user
    with pytest.raises(ValueError):
        user_profile(token, 4)
        


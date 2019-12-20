import pytest

from user_profile_setname import user_profile_setname
from auth_login import auth_login
from user_profile_setemail import user_profile_setemail
from auth_register import auth_register

user = auth_register('valid_email@email.com', 'valid_password', 'valid_first', 'valid_last')
res2 = auth_login('valid_email@email.com', 'valid_password')
token1 = res2['token']
u_id = res2['u_id']

def test_user_profile_setemail_1():
    #testing valid case
    with pytest.raises(ValueError):
        assert user_profile_setemail(token1, "invalidemail.edu.au")
        
    
def test_user_setemail():
    #Email entered is already there.
    with pytest.raises(ValueError):
        user_profile_setemail(token1, "valid_email@email.com")
        
        
def test_user_profile_setemail_3():    
    #Email address is already being used by another user
    assert user_profile_setemail(token1, "cs2521@unsw.edu.au") == {}
    


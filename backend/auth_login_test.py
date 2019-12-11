import pytest

from auth_login import auth_login
from auth_register import auth_register
from GLOBAL import GLOBAL_DATA , User, generate_token, generate_user_id

# Register user
user1 = auth_register('valid_email@email.com', 'valid_password', 'valid_first', 'valid_last')

user2 = auth_register('valid_email2@email.com', 'valid_password2', 'valid_first2', 'valid_last2')

def test_auth_login_incorrect_password():
    # Test incorrect password for a valid user
    with pytest.raises(ValueError):
        auth_login('valid_email@email.com', 'incorrect_password')     

def test_auth_login_invalid_email():
    # Test invalid input for email
    with pytest.raises(ValueError):
        auth_login('invalid_email', 'valid_password')          

def test_auth_login_nonuser():
    # Test email that does not belong to a user
    with pytest.raises(ValueError):
        auth_login('non_user@email.com', 'valid_password')

def test_auth_login_valid():
    # Test valid email and password
    assert auth_login('valid_email@email.com', 'valid_password') == { 'u_id': user1['u_id'], 'token': user1['token'] }   

def test_auth_login_valid2():
    # Test valid email and password
    assert auth_login('valid_email2@email.com', 'valid_password2') == { 'u_id': user2['u_id'], 'token': user2['token'] }   

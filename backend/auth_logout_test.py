from auth_login import auth_login
from auth_logout import auth_logout
from auth_register import auth_register
from GLOBAL import GLOBAL_DATA , User, generate_token, generate_user_id

# Register a user with valid credentials and log them in
user1 = auth_register('valid_email1@email.com', 'valid_password1', 'valid_first1', 'valid_last1')
res1 = auth_login('valid_email1@email.com', 'valid_password1')
token1 = user1['token']

def test_auth_logout_active_token():
    # Test an active token
    assert auth_logout(token1) == { 'is_success': True }

def test_auth_logout_inactive_token():
    # Test an inactive token
    assert auth_logout(token1) == { 'is_success': False }

# Assuming all tokens will be valid

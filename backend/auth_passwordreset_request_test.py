from auth_login import auth_login
from auth_passwordreset_request import auth_password_reset_req
from auth_register import auth_register
import pytest

# Register a user with valid credentials and log them in
user1 = auth_register('bob.ma77i@gmail.com', 'valid_password1', 'valid_first1', 'valid_last1')
res1 = auth_login('bob.ma77i@gmail.com', 'valid_password1')

def test_auth_passwordreset_request_valid_user():
    # Test a valid email belonging to a registered user
    assert auth_password_reset_req('bob.ma77i@gmail.com') == {}

def test_auth_passwordreset_request_non_user():
    # Test a valid email that does not belong to a registered user
    with pytest.raises(ValueError):
        auth_password_reset_req('non_user@email.com')


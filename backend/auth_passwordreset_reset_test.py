import pytest
import hashlib

from GLOBAL import GLOBAL_DATA , User, generate_token, generate_user_id

from auth_login import auth_login
from auth_passwordreset_request import auth_password_reset_req
from auth_passwordreset_reset import auth_password_reset
from auth_register import auth_register

# Register a user with valid credentials, log them in and request a password reset
user1 = auth_register("valid_email1@email.com", "valid_password1", "valid_first1", "valid_last1")
res1 = auth_login("valid_email1@email.com", "valid_password1")
auth_password_reset_req("valid_email1@email.com")

# How to get the actual reset code????
def test_auth_password_reset_valid():
    user_email = "valid_email1@email.com"
    code = hashlib.sha256(user_email.encode()).hexdigest()
    # Test valid reset code and new password (5 character length boundary test)
    assert auth_password_reset(code, "new_password123") == {}

def test_auth_password_reset_invalid_code():
    # Test invalid reset code
    with pytest.raises(ValueError):
        auth_password_reset("invalid_reset_code", "new_password123")

def test_auth_password_reset_invalid_new_password():
    # Test invalid 4 character new password (5 character length boundary test)
    with pytest.raises(ValueError):
        auth_password_reset("valid_reset_code", "abcd")

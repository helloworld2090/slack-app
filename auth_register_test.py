import pytest

from auth_register import auth_register
import sys
sys.path.append('..')
from GLOBAL import GLOBAL_DATA, User, generate_token, generate_user_id

def test_auth_register_valid():
    # Test valid email, password, name_first and name_last at boundaries
    assert auth_register('user@email.com', 'abcdefr',
                '49_character_firstname',
                '49_character_lastname') == { 'u_id': 0, 'token': generate_token('user@email.com') }


def test_auth_register_invalid_email():
    # Test invalid email
    with pytest.raises(ValueError):
        auth_register('invalid_email', 'abcdef', 'Firstname', 'Lastname')

def test_auth_register_invalid_password():
    # Test invalid 4 character password (6 character boundary test)
    with pytest.raises(ValueError):
        auth_register('nonuser@email.com', 'abde', 'Firstname', 'Lastname')

def test_auth_register_invalid_firstname():
    # Test invalid 50 character first name (50 character boundary test)
    with pytest.raises(ValueError):
        auth_register('nonuser@email.com', 'abcdef', '51_character_firstname_0123456789012345678901234567', 'Lastname')

def test_auth_register_invalid_lastname():
    # Test invalid 50 character last name (50 character boundary test)
    with pytest.raises(ValueError):
        auth_register('nonuser@email.com', 'abcdef', 'Firstname', '51_character_lastname_01234567890123456789012345678')

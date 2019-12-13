import pytest

from auth_login import auth_login
from auth_register import auth_register
from channel_create import channel_create

# Create channel owner
user1 = auth_register('valid_email1@email.com', 'valid_password1', 'valid_first1', 'valid_last1')
res1 = auth_login('valid_email1@email.com', 'valid_password1')
token1 = res1['token']

def test_channels_create_valid_public():
    # Test creating a valid public channel (with name at 20 char boundary)
    assert channel_create(token1, '20charactername_abcd', True) == { 'channel_id': 0 }

def test_channel_create_valid_private():
    # Test creating a valid private channel (with name at 20 char boundary)
    assert channel_create(token1, '20charactername_efgh', False) == { 'channel_id': 1 }

def test_channel_create_valid_duplicate():
    # Test creating a channel with the name of an existing one
    assert channel_create(token1, '20charactername_abcd', True) == { 'channel_id': 2 }

def test_channel_create_invalid_name():
    # Test creating an invalid channel with a name too long (>20 char boundary)
    with pytest.raises(ValueError):
        channel_create(token1, '21charactername_abcde', True)

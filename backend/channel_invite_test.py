import pytest

from auth_login import auth_login
from auth_register import auth_register
from channel_invite import channel_invite
from channel_create import channel_create
from Error import AccessError

# Create channel owner
user1 = auth_register('valid_email1@email.com', 'valid_password1', 'valid_first1', 'valid_last1')
res1 = auth_login('valid_email1@email.com', 'valid_password1')
token1 = res1['token']
channel_id1 = channel_create(token1, 'Example channel 1', True)['channel_id']

# Create user to be invited
user2 = auth_register('valid_email2@email.com', 'valid_password2', 'valid_first2', 'valid_last2')
res2 = auth_login('valid_email2@email.com', 'valid_password2')
token2 = res2['token']
u_id2 = res2['u_id']

# Create new user who owns a different channel
user3 = auth_register('valid_email3@email.com', 'valid_password3', 'valid_first3', 'valid_last3')
res3 = auth_login('valid_email3@email.com', 'valid_password3')
token3 = res3['token']
channel_id3 = channel_create(token3, 'Example channel 3', True)['channel_id']

def test_channel_invite_valid():
    # Test valid token, user id and channel id
    assert channel_invite(token1, channel_id1, u_id2) == {}

def test_channel_invite_inviting_self():
    # Test a user inviting themselves 
    with pytest.raises(AccessError):
        channel_invite(token2, channel_id1, u_id2)

def test_channel_invite_non_auth():
    # Test channel id for a channel the authorised user is not part of 
    with pytest.raises(AccessError):
        channel_invite(token3, channel_id1, u_id2)

def test_channel_invite_invalid_u_id():
    invalid_u_id = -1
    # Test user id which does not refer to a valid user
    with pytest.raises(ValueError):
        channel_invite(token1, channel_id1, invalid_u_id)

def test_channel_invite_channel():
    invalid_channel_id = -1
    # Test channel id which does not refer to a valid channel
    with pytest.raises(ValueError):
        channel_invite(token1, invalid_channel_id, u_id2)

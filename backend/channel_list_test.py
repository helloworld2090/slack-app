import pytest

from auth_login import auth_login
from auth_register import auth_register
from channel_invite import channel_invite
from channel_create import channel_create
from channels_list import channels_list

# Create channel owner
user1 = auth_register('valid_email1@email.com', 'valid_password1', 'valid_first1', 'valid_last1')
res1 = auth_login('valid_email1@email.com', 'valid_password1')
token1 = res1['token']
u_id1 = res1['u_id']

# Create user to be invited
user2 = auth_register('valid_email2@email.com', 'valid_password2', 'valid_first2', 'valid_last2')
res2 = auth_login('valid_email2@email.com', 'valid_password2')
token2 = res2['token']
u_id2 = res2['u_id']


def test_channels_list_no_channels():
    # Test a user in no channels
    assert channels_list(token2) == { 'channels': [] }
    
channel_id1 = channel_create(token1, 'Example channel 1', True)['channel_id']

def test_channels_list_own_channel():
    
    # Test a user who has created their own channel
    assert channels_list(token1) == { 'channels': [{ 'id': channel_id1, 'name': 'Example channel 1' }] }

def test_channels_list_invited_user():
    # Test a user who has been invited to a channel
    channel_invite(token1, channel_id1, u_id2)
    assert channels_list(token2) == { 'channels': [{ 'id': channel_id1, 'name': 'Example channel 1' }] }

def test_channels_list_multiple_channels():
    # Test a user who is in multple channels (invited and created)
    channel_id2 = channel_create(token2, 'Example channel 2', True)['channel_id']
    assert channels_list(token2) == { 'channels': [
        { 'id': channel_id1, 'name': 'Example channel 1' },
        { 'id': channel_id2, 'name': 'Example channel 2' },
    ]}

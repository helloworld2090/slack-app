import pytest

from auth_login import auth_login
from auth_register import auth_register
from channel_invite import channel_invite
from channel_create import channel_create
from channels_listall import channels_listall

# Create channel owner
user1 = auth_register('valid_email1@email.com', 'valid_password1', 'valid_first1', 'valid_last1')
res1 = auth_login('valid_email1@email.com', 'valid_password1')
token1 = res1['token']

# Create user to be invited
user2 = auth_register('valid_email2@email.com', 'valid_password2', 'valid_first2', 'valid_last2')
res2 = auth_login('valid_email2@email.com', 'valid_password2')
token2 = res2['token']
u_id2 = res2['u_id']

def test_channels_listall_no_channels():
    # Test where no channels exist
    assert channels_listall(token1) == { 'channels': [] }

def test_channels_listall_one_channel():
    # Test once one channel has been created (from the creator account)
    global channel_id1
    channel_id1 = channel_create(token1, 'Example channel 1', True)['channel_id']
    assert channels_listall(token1) == { 'channels': [{ 'id': channel_id1, 'name': 'Example channel 1' }] }

def test_channels_listall_other_users_channel():
    # Test once one channel has been created (from another account which is not in the channel)
    assert channels_listall(token2) == { 'channels': [{ 'id': channel_id1, 'name': 'Example channel 1' }] }

def test_channels_listall_multiple_users():
    # Test the same user once they have been added to the channel
    channel_invite(token1, channel_id1, u_id2)
    assert channels_listall(token2) == { 'channels': [{ 'id': channel_id1, 'name': 'Example channel 1' }] }

def test_channels_listall_multiple_channels():
    # Test there being multiple channels
    channel_id2 = channel_create(token2, 'Example channel 2', True)['channel_id']
    assert channels_listall(token2) == { 'channels': [
        { 'id': channel_id1, 'name': 'Example channel 1' },
        { 'id': channel_id2, 'name': 'Example channel 2' },
    ]} 

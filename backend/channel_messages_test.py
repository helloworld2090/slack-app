import datetime

import pytest

from auth_login import auth_login
from auth_register import auth_register
from channel_messages import channel_messages
from channel_create import channel_create
from Error import AccessError
#from message_send import message_send

# Create channel owner
user1 = auth_register('valid_email1@email.com', 'valid_password1', 'valid_first1', 'valid_last1')
res1 = auth_login('valid_email1@email.com', 'valid_password1')
u_id1 = res1['u_id']
token1 = res1['token']
channel_id1 = channel_create(token1, 'Example channel 1', True)['channel_id']

# Create additional user
user2 = auth_register('valid_email2@email.com', 'valid_password2', 'valid_first2', 'valid_last2')
res2 = auth_login('valid_email2@email.com', 'valid_password2')
token2 = res2['token']
u_id2 = res2['u_id']

start = 0
message = { 'message_id': 0, 'u_id': u_id1, 'message': 'test_message', 
        'time_created': datetime.datetime.now(), 'is_unread': True }

def test_channel_messages_no_messages():
    # Test channel with no messages
    start = 0
    assert channel_messages(token1, channel_id1, start) == { 'messages': [], 'start': 0, 'end': -1 }

def test_channel_messages_invalid_start():
    # Test channel with no messages and a start value greater than the total number of messages in the channel
    start = 1 # at boundary of total messages
    with pytest.raises(ValueError):
        channel_messages(token1, channel_id1, start)

def test_channel_messages_invalid_channel():
    # Test channel which doesn't exist
    invalid_channel_id = -1
    start = 0
    with pytest.raises(ValueError):
        channel_messages(token1, invalid_channel_id, start)

def test_channel_messages_non_member():
    # Test channel which authorised user is not a member of 
    with pytest.raises(AccessError):
        channel_messages(token2, channel_id1, start)
"""
def test_channel_messages_reach_end():
    # Add a message to the channel and test
    message_send(token1, channel_id1, message)
    start = 0
    assert channel_messages(token1, channel_id1, start) == { 'messages': [message], 'start': 0, 'end': -1 }

def test_channel_messages_more_than_50():
    # Add 50 messages (boundary of start/end difference) and test
    testMessages = []
    for _ in range(50):
        message['message_id'] += 1
        message_send(token1, channel_id1, message)
        
        testMessages.append(message)

    start = 0
    assert channel_messages(token1, channel_id1, start) == { 'messages': testMessages, 'start': 0, 'end': 50 }

    # Test start > 0 to end of messages
    message['message_id'] += 1
    message_send(token1, channel_id1, message)
    testMessages.append(message)
    testMessages.pop(0) # Remove first message which wont get returned when start = 1

    start = 1
    assert channel_messages(token1, channel_id1, start) == { 'messages': testMessages, 'start': 1, 'end': 51 }
"""
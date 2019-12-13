import pytest
from Error import AccessError

from auth_login import auth_login
from auth_register import auth_register
from channel_leave import channel_leave
from channel_create import channel_create
from channel_join import channel_join

# Create channel owner
user1 = auth_register('valid_email1@email.com', 'valid_password1', 'valid_first1', 'valid_last1')
res1 = auth_login('valid_email1@email.com', 'valid_password1')
token1 = res1['token']
channel_id1 = channel_create(token1, 'Example channel 1', True)['channel_id']

# Create additional user and invite them to channel_id1
user2 = auth_register('valid_email2@email.com', 'valid_password2', 'valid_first2', 'valid_last2')
res2 = auth_login('valid_email2@email.com', 'valid_password2')
token2 = res2['token']
u_id2 = res2['u_id']
channel_join(token2, channel_id1)

# Create user who is not a member of channel_id1
user3 = auth_register('valid_email3@email.com', 'valid_password3', 'valid_first3', 'valid_last3')
res3 = auth_login('valid_email3@email.com', 'valid_password3')
token3 = res3['token']

def test_channel_leave_valid():
    # Test valid channel id that the authorised user is a member of
    assert channel_leave(token2, channel_id1) == {}

def test_channel_leave_AccessError():
    # Test valid channel id that the authorised user is a member of
    with pytest.raises(AccessError):
        channel_leave(token3, channel_id1)
    
def test_channel_leave_invalid_channel():
    # Test leaving a channel that does not exist
    invalid_channel_id = -1
    with pytest.raises(ValueError):
        channel_leave(token1, invalid_channel_id)

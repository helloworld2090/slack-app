import pytest

from auth_login import auth_login
from auth_register import auth_register
from channel_join import channel_join
from channel_create import channel_create
from Error import AccessError

# Create channel owner
user1 = auth_register('valid_email1@email.com', 'valid_password1', 'valid_first1', 'valid_last1')
res1 = auth_login('valid_email1@email.com', 'valid_password1')
token1 = res1['token']
channel_id1 = channel_create(token1, 'Example channel 1', True)['channel_id']

# Create additional user
user2 = auth_register('valid_email2@email.com', 'valid_password2', 'valid_first2', 'valid_last2')
res2 = auth_login('valid_email2@email.com', 'valid_password2')
token2 = res2['token']
u_id2 = res2['u_id']


def test_channel_join_valid():
    # Test valid user who can join public channel
    assert channel_join(token2, channel_id1) == {}

def test_channel_join_invalid_channel():
    # Test channel which does not exist
    invalid_channel_id = -1
    with pytest.raises(ValueError):
        channel_join(token2, invalid_channel_id)
        
def test_channel_join_private_channel():
    # Test channel which the user cannot join (private channel and user is not an admin)
    channel_id2 = channel_create(token2, 'Private channel 2', False)['channel_id']
    with pytest.raises(AccessError):
        channel_join(token1, channel_id2)


import pytest

from auth_login import auth_login
from auth_register import auth_register
from channel_addowner import channel_addowner
from channel_create import channel_create
from Error import AccessError

# Create channel owner
user1 = auth_register('valid_email1@email.com', 'valid_password1', 'valid_first1', 'valid_last1')
res1 = auth_login('valid_email1@email.com', 'valid_password1')
token1 = res1['token']
u_id1 = res1['u_id']
channel_id1 = channel_create(token1, 'Example channel 1', True)['channel_id']

# Create user to be made owner
user2 = auth_register('valid_email2@email.com', 'valid_password2', 'valid_first2', 'valid_last2')
res2 = auth_login('valid_email2@email.com', 'valid_password2')
token2 = res2['token']
u_id2 = res2['u_id']

# Create a third user in no channels
user3 = auth_register('valid_email3@email.com', 'valid_password3', 'valid_first3', 'valid_last3')
res3 = auth_login('valid_email3@email.com', 'valid_password3')
token3 = res3['token']
u_id3 = res3['u_id']

def test_channel_addowner_non_owner():
    # Test an authorised user who is not an owner (and hence cannot give owner permissions to others)
    with pytest.raises(AccessError):
        channel_addowner(token2, channel_id1, u_id3)

def test_channel_addowner_valid():
    # Test with a non-owner (to become an owner) and a valid channel
    assert channel_addowner(token1, channel_id1, u_id2) == {}

def test_channel_addowner_invalid_channel():
    # Test a channel that does not exist
    invalid_channel_id = -1
    with pytest.raises(ValueError):
        channel_addowner(token1, invalid_channel_id, u_id2)

def test_channel_addowner_already_owner():
    # Test a user who is already an owner of the channel
    with pytest.raises(ValueError):
        channel_addowner(token1, channel_id1, u_id2)

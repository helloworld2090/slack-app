import pytest

from auth_login import auth_login
from auth_register import auth_register
from channel_details import channel_details
from channel_invite import channel_invite
from channel_create import channel_create
from Error import AccessError

# Create channel owner
user1 = auth_register('valid_email1@email.com', 'valid_password1', 'valid_first1', 'valid_last1')
res1 = auth_login('valid_email1@email.com', 'valid_password1')
token1 = res1['token']
u_id1 = res1['u_id']
channel_id1 = channel_create(token1, 'Example channel 1', True)['channel_id']

# Create user to be invited
user2 = auth_register('valid_email2@email.com', 'valid_password2', 'valid_first2', 'valid_last2')
res2 = auth_login('valid_email2@email.com', 'valid_password2')
token2 = res2['token']
u_id2 = res2['u_id']

user1 = { 'u_id': user1, 'name_first': 'valid_first1', 'name_last': 'valid_last1' }
user2 = { 'u_id': user2, 'name_first': 'valid_first2', 'name_last': 'valid_last2' }

def test_channel_details_valid_owner():
    # Test valid token and channel id
    assert channel_details(token1, channel_id1) == {
        'name': 'Example channel 1',
        'owner_members': [user1['name_first']],
        'all_members': [user1['name_first']],
    }

def test_channel_details_non_member():
    # Test id of a channel which the authorised user is not a member of
    with pytest.raises(AccessError):
        channel_details(token2, channel_id1)

def test_channel_details_new_member():
    # Test a newly added member
    channel_invite(token1, channel_id1, u_id2)
    assert channel_details(token1, channel_id1) == {
        'name': 'Example channel 1',
        'owner_members': [user1['name_first']],
        'all_members': [user1['name_first'], user2['name_first']],
    }

def test_channel_details_invalid_channel():
    invalid_channel_id = -1
    # Test id of a channel that doesnt exist
    with pytest.raises(ValueError):
        channel_details(token1, invalid_channel_id)


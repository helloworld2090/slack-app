import pytest

from auth_login import auth_login
from auth_register import auth_register
from channel_create import channel_create
from message_send import message_send
from channel_join import channel_join
from message_edit import message_edit

from Error import AccessError

user1 = auth_register("valid_email1@email.com", "valid_password1", "valid_first1", "valid_last1")
res1 = auth_login("valid_email1@email.com", "valid_password1")
token1 = res1["token"]
channel_id1 = channel_create(token1, "Example channel 1", True)["channel_id"]

# Create additional user
user2 = auth_register("valid_email2@email.com", "valid_password2", "valid_first2", "valid_last2")
res2 = auth_login("valid_email2@email.com", "valid_password2")
token2 = res2["token"]
u_id2 = res2["u_id"]



    # Add messages data
def test_message_edit():
    message_send(token1, channel_id1, "test_message1") # assume message id 0
    channel_join(token2, channel_id1)
    message_send(token2, channel_id1, "test_message2") # assume message id 1
    # Test valid message edit
    assert message_edit(token1, 0, "edited_test_message1") == {}

    # Test message that wasn't made by the authorised user (who is not an owner/admin)

def test_message_non_auth():
    with pytest.raises(AccessError):
        message_edit(token2, 0, "edited_test-message1")

    # Test message that wasn't made by the authorised user (who is an owner/admin)

def test_message_owner():
    message_send(token2, channel_id1, "test_message2") # assume message id 1
    message_edit(token1, 2, "")
    return {}

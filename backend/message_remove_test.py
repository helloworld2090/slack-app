import pytest

from auth_login import auth_login
from auth_register import auth_register
from channel_create import channel_create
from Error import AccessError
from message_send import message_send
from message_remove import message_remove

# Create channel owner
user1 = auth_register("valid_email1@email.com", "valid_password1", "valid_first1", "valid_last1")
res1 = auth_login("valid_email1@email.com", "valid_password1")
token1 = res1["token"]
channel_id1 = channel_create(token1, "Example channel 1", True)

# Create additional user
user2 = auth_register("valid_email2@email.com", "valid_password2", "valid_first2", "valid_last2")
res2 = auth_login("valid_email2@email.com", "valid_password2")
token2 = res2["token"]
u_id2 = res2["u_id"]

def test_message_remove0():

    # Add messages data                                                                 
    message_send(token1, 0, "test_message1") # assume message id 0
    message_send(token1, 0, "test_message2") # assume message id 1
                        
    # Test valid message removal    
    assert message_remove(token1, 1) == {}


def test_message_remove_non_admin():
    message_send(token1, 0, "test_message3") # assume message id 3
    # Test message that wasn't made by the authorised user (who is not an owner/admin)
    with pytest.raises(AccessError):
        message_remove(token2, 0)

def test_message_remove3():
    # Test message that wasn't made by the authorised user (who is an owner/admin)
    message_send(token1, 0, "test_message3") # assume message id 3
    message_send(token1, 0, "test_message3") # assume message id 3
    assert message_remove(token1, 3) == {}


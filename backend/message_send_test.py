import pytest
from Error import AccessError
from auth_login import auth_login
from auth_register import auth_register
from channel_create import channel_create
from message_send import message_send

# Create channel owner
user1 = auth_register("valid_email1@email.com", "valid_password1", "valid_first1", "valid_last1")
res1 = auth_login("valid_email1@email.com", "valid_password1")
token1 = res1["token"]
channel_id1 = channel_create(token1, "Example channel 1", True)

user2 = auth_register("valid_email2@email.com", "valid_password2", "valid_first2", "valid_last2")
res2 = auth_login("valid_email2@email.com", "valid_password2")
token2 = res2["token"] 

def test_message_send():

    # Test a valid message to a channel an authorised used is a member of
    assert message_send(token1, 0, "test_message") == {"message_id": 0}


def test_message_again():
    # testing second valid message with id == 1
    assert message_send(token1, 0, "test_message2") == {"message_id": 1}

def test_message_again2():
    # testing second valid message with id == 1
    assert message_send(token1, 0, "test_message2") == {"message_id": 2}


def test_message_error():
    # testing invalid message with length exceeding the maximum
    with pytest.raises(ValueError):
        assert message_send(token1, 0, "I"*1001)

def test_message_AccessError():
    # testing Access error for user who is not in the channel
    with pytest.raises(AccessError):
        assert message_send(token2 , 0, "message")
        
        


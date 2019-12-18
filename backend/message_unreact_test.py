import pytest

from auth_login import auth_login
from auth_register import auth_register
from channel_create import channel_create
from message_send import message_send
from channel_join import channel_join
from message_edit import message_edit
from message_react import message_react
from message_unreact import message_unreact

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

def test_message_unreact():
    message_send(token1, 0, "test_message")
    message_send(token1, 0, "test_message2") # assume message id 2
    message_send(token1, 0, "test_message3") # assume message id 2
    message_react(token1, 0, 1) 
    assert message_unreact(token1, 0, 0) == {}

def test_message_already_unreacted():
    with pytest.raises(ValueError):
        message_unreact(token1, 0, 0)
       

def test_message_unreact_invalid_msg_id():
    with pytest.raises(ValueError):
        message_unreact(token1, 3, 0)

def test_message_unreact_invalid_react_id():
    message_send(token1, 0, "test_message")
    # test an invalid message Id case
    with pytest.raises(ValueError):
        message_react(token1, 0, -1)

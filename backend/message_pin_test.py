import pytest

from auth_login import auth_login
from auth_register import auth_register
from channel_create import channel_create
from message_send import message_send
from channel_join import channel_join
from message_edit import message_edit
from message_react import message_react
from message_pin import message_pin

from Error import AccessError

user1 = auth_register("valid_email1@email.com", "valid_password1", "valid_first1", "valid_last1")
res1 = auth_login("valid_email1@email.com", "valid_password1")
token1 = res1["token"]
channel_create(token1, "Example channel 1", True)["channel_id"]

# Create additional user
user2 = auth_register("valid_email2@email.com", "valid_password2", "valid_first2", "valid_last2")
res2 = auth_login("valid_email2@email.com", "valid_password2")
token2 = res2["token"]
u_id2 = res2["u_id"]

def test_message_pin():
    message_send(token1, 0, "test_message")
    message_send(token1, 0, "test_message2") # assume message id 2
    message_send(token1, 0, "test_message3") # assume message id 2
    assert message_pin(token1, 0) == {}

def test_message_already_pinned():
    with pytest.raises(ValueError):
        message_pin(token1, 0)
       

def test_message_react_invalid_msg_id():
    with pytest.raises(ValueError):
        message_pin(token1, -1)

def test_message_react_non_admin():
    # test an invalid message Id case
    with pytest.raises(ValueError):
        message_pin(token2,1)

def test_admin_but_non_members():
    channel_id2 = channel_create(token2, "Example channel 2", True)["channel_id"]
    m_id = message_send(token2, channel_id2, "test_message")["message_id"]
    with pytest.raises(AccessError):
        message_pin(token1, m_id)





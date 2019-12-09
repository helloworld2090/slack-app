# Assumptions

- front end GUI does not allow users to perform invalid actions including:
    - message actions (e.g. sending, removing) in channels which do not exist or the user is not a member/admin/owner of
    - editing messages which have been removed
    - leaving required fields empty (e.g. password when registering)
    - invalid channel actions such users joining channels they're in or leaving channels they're not in
- all data in tests only exists within tests for that specific function
- all data passed into functions will be of the right type
- data passed into functions cannot be null or empty (e.g. "")
- all tokens returned by auth_login() will always be valid and active unless the user is logged out by calling auth_logout()
- tokens returned will be from a secure hash function 
- multiple channels of the same name can be created and they will all return a unique channel_id
- the u_id passed into channel_addowner and channel_removeowner must already be a member of the channel (but can have any permissions)
- messages sent in a channel will have consecutive id's where the first message sent in the channel has an id 0
- search can handle multiple keywords and the function will search for each word seperately and match messages that contain all words
- url passed into user_profiles_uploadphoto will always be a valid image url
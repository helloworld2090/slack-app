## How our backend implementation is fit for purpose
 

## Verification and validation 

Epic 1: As a member I want to be able to use Slackr so I connect with UNSW staff and classmates. 

1.1 As a member I want to be able to register so that I can make my own account with my own personal details.

- There is a register button in a navigation bar
- Clicking register displays a form where the user can enter their first name, last name, email and password
- Users can register if all the fields are filled with valid data  
- Each input field has a relevant placeholder which disappears when the user starts typing
- Password strength is displayed

1.2 As a member I want to be able to login into my account so that I can access my course discussion and for my future work.

- There is a login button in the navigation bar
- Clicking login displays a page where the user can enter their email and password
- Users can login if the fields have valid data
- Each input field has a relevant placeholder which disappears when the user starts typing

1.3 As a member I want to be able to log out of my account so that I can exit Slackr when I want to.
- There is a logout button in the navigation bar if the user is currently logged in
- Clicking logout redirects the user to the homepage
- Logging out deletes all locally stored user data

1.4 As a member I want to be able to reset my password so that if I forget, I will be able to recover my account.
- There is a “reset password” button in the login form
- Clicking “reset password” updates the form to show only an email field and “send reset code” button
- A reset code will be sent to the provided email when “send reset code” button is pressed
- The form will display an input field to enter reset code
- Upon entering a valid reset code an input field to enter a new password will be displayed
- Password strength is displayed
- The new password cannot be the same as the old one
- Each input field has a relevant placeholder which disappears when the user starts typing


1.5 As a member I want to be able to see a list of channels so that I can see which channels I can join and which channels are most suitable for me.

- There is a “display channels” button visible to logged in users
- An infinitely scrolling list shows the name and basic details about all channels

1.6 As a member I want to be able to create a channel so that I can invite my classmates and hold discussions on my channel.

- There is a “create channel” button visible to logged in users
- Clicking “create channel” displays a form where the user can enter a channel name and toggle between public and private
- Creating a channel adds the user to the channel’s members and owners list
- Each input field has a relevant placeholder which disappears when the user starts typing

1.7 As a member I want to be able to join a channel so that I can join discussions with my classmates and university staff.
- There is a join button beside each channel displayed in the channels list
- Joining a channel allows the user to view existing messages from fellow channel members and send new messages

1.8 As a member I want to be able to invite someone to a channel so that I can add my group members.
- There is an invite button visible to logged in users who are viewing a channel they are a member of
- There is an add button at the top bar	


1.9 As a member I want to be able to leave a channel when I am finished with the project or class.
- There is a “leave channel” button visible to logged in users who are viewing a channel they are a member of
- Clicking “leave channel” displays a confirmation 
- Leaving the channel removes the member’s name from the channel’s member list and removes references to the channel for the member

1.10 As a member I want to be able to easily view the messages so that I can read the discussions to learn from my channel members.
- A list of channels will be displayed 
- Messages will also be displayed 

1.11 As a member I want to be able to view the members of the channel so that I can allocate roles and add new members when needed. 
- A list of members will be displayed 
- Add button will pop up on the top bar

1.12 As a member I want to be able to view the details of the channel so that I can use features that may be of use that I wasn't aware of before.
- Features of each channel will be displayed when clicking on that specific channel

1.13 As a member I want to be able to send a message or send a message at a specified time in the future so that I can get an important message through as soon as possible and also have the ability to relay messages at a future time.
- Messages will be sent by clicking the “send” button
- The timer will be displayed when the user clicks the “specified time” feature 

1.14 As a member I want to be able to edit, remove, pin, unpin, react, or unreact to a message so that I can fix a mistake, emphasise the importance of the message in the group chat and interact with message in a fun way.
- Edit, remove, pin, unpin, react button will be displayed below the electronic keyboard
- The edit button brings the user to the message, with the ability to change the message

1.15 As a member I want to be able to search messages using a search string so I can quickly search for messages I want to view.
- The search field is placed on the top bar
- Search starts once the user clicks “Search”

1.16 As a member I want to be able to view anyone's user profile, and modify a user's own profile so that I can view who I can work with, I can update my personal details so that other people can identify who I am, I can contact them in the case where I can relay important information to them.
- User views anyone’s profile by clicking their profile picture
- User can change their personal details by clicking on their own profile picture or by clicking “profile”
- Clicking on another’s profile will have a “message” button 

1.17 As a member I want to be able to begin a “Standup” so I have quick and informative discussions with my peers and also read the summaries of past Standups.  
- Standup is performed by clicking “standup”
- After standup is performed, a link to the summary of past standups will appear


Epic 2: As an admin I want to be able to organise members and channels on Slackr to ensure things run smoothly.

2.1 As an admin I want to be able to login into my account so that I can view what type of projects assigned by UNSW and communicate them with tutors and other academic staff. 
- There is a login button on the navigation bar 
- Clicking the login button will show a page where the user can view projects that are assigned by UNSW
- A list of projects is displayed in the sidebar 

2.2 As an admin I want to be able to reset my password so that I can regularly reset my password to prevent unauthorised access to my account. 
- There is a “reset password” button in the login form
- Clicking “reset password” updates the form to show only an email field and “send reset code” button
- A reset code will be sent to the provided email when “send reset code” button is pressed
- The form will display an input field to enter reset code
- Upon entering a valid reset code an input field to enter a new password will be displayed
- Password strength is displayed
- The new password cannot be the same as the old one
- Each input field has a relevant placeholder which disappears when the user starts typing

2.3 As an admin I want to be able to search and view a list of channels so I can keep track of the channels created. 
- Enter the search term in the search field (in the header) will filter the list of channels
- The list of channels will be displayed
- Search starts once the user clicks “Search”
- The field contains a placeholder with a grey-colored text: “Where are you going?”  
- The placeholder disappears once the user starts typing
- Search is performed if a user types in a channel
- The user can’t type more than 200 characters 

2.4 As an admin I want to be able to create a channel so I can invite staff and students to join.
- The “create a channel” button is placed on the top bar
- Creating a channel is performed if the user clicks the button
- Inviting staff or students will display “You have invited someone to your channel”

2.5 As an admin I want to be able to view all messages so that I am informed about updates from my colleagues. 
- A list of channels will be displayed 
- Messages will be displayed 
- Popups from certain group members will have bold messages on the sidebar

2.6 As an admin I want to be able to send a message instantly and at a specified time in the future so that I can communicate with my colleagues.
- Messages will be sent by clicking the “message” button
- The “specified time” feature will be shown on the bottom corner

2.7 As an admin I want to be able to view the members of the channel so that I can know who has joined a channel.
- A list of members of the channel will be displayed 
- Clicking the “details” of the channel will show which members are online and all the members who have joined the channel

2.8 As an admin I want to the ability to modify accounts within the systems, so that I can view and manually update users, information, roles, sections, courses, enrolments.
- Clicking the account of oneself will display features in the systems 
- Account settings enable the user to change the details of the account
 
Epic 3: As an owner I want to be able to manage Slackr to ensure it achieves UNSW's strategic objectives. 

3.1 As an Owner I want to be able to register into an account so that can communicate with Admins and members.
- “Register” button will be displayed when registering
- Credentials will be required in order to allow the user to enter the account in Slackr

3.2 As an Owner I want to be able to reset my password so regularly change my password to make to account more secure.
- Password reset option available
- Must be able to change at least daily

3.3 As an Owner I want to be able to view all messages of the channel so that I can create and maintain the product.
- Owners have highest level of permission
- All messages can be seen by owners

3.4 As an Owner I want to be able to view the details of the channel for my team so that I can validate the productivity of users on Slackr and draw comparisons with key performance indicators. 
- Only shows for Owners
- Quantitative descriptors for each team members’ contributions


## Strategies
To start iteration 2, we held a group meeting and discussed the project requirements and specifications and our strengths and weaknesses. From this we allocated functions to members based on our strengths and preferences. Furthermore, we held multiple online discussions via messenger where group members could seek help and gather input from other members. This allowed us to work more productivity and coherently as members were less likely to be stuck writing a time consuming function. 
Another strategy used where the high frequency of git commit to our group repository, which allowed members to be more updated with the rest of the group and their code. This also allowed members to spot mistakes early in the development of our functions, which reduced time spent on debugging or rewriting entire functions. 

## Tools we used

While writing our functions we regularly ran the server and used Postman to send requests. By observing the return data we could ensure our functions were compliant with the project spec. We also regularly used pytest to test our functions against the different paths and boundary cases we set up in iteration 1.

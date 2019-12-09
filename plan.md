# Plan

plan.md (Write a brief 1-page plan highlighting how you will approach the following iteration (the development stage).

We will approach the following iteration with the same plan as the first iteration, working concurrently on the individual components.  The main reasoning is that if we were to split roles equally among group members, some tasks may overlap or end up not being useful and different members may think of more efficient ways of doing things.

We will be referring to lecture slides, the tut notes, and internet pages regarding creating each individual function in a clean and efficient way.

The next iteration will most likely change based on feedback from the first iteration.  We are trying to create an application or a system that is ready to use while at the same time avoiding major bugs so that makes the users are happy and willing to use it. To achieve this, it is likely that we will be referring heavily to iteration 1 and its feedback in the development stage.  We will definitely use the user stories to ensure that the requirements fit the users' needs and improve product usability, thus making the application as user-friendly as possible.  

For the development stage we hope to achieve our goal in a more efficient way as compared to iteration 1.  First we will plan on meeting the whole group more frequently and divide roles equally among group members.  It is possible that one person may not be on top of his individual work, so we plan on gathering the whole group and renegotiating a solution if such a problem occurs.  There can be many reasons why one person may not know how to approach or finish his part, e.g. External factors such as family business which restricts them from doing their work, but we will focus first and foremost on completing the tasks to theb est of our ability.

As for time estimation, we estimate, and in the order in which we would implement them:

The following functions are very basic and are required to formulate a basic messaging system. It will take a day or two to work through these ans establish a framework, but discussions will take place beforehand and during the design process to ensure smooth progression

auth_login
auth_register
auth_passwordreset_request
channels_create
auth_logout
channel_invite
channel_join
channel_leave
channel_addowner
message_send

These functions deal with finding a set of data and modifying it in some way. They require the basic functions above and occasionally the search function, which is to be completed first. Once search is completed, we estimate that several days solid work are required to complete the others.

search- 2 hours

auth_passwordreset_reset
channel_removeowner
message_remove
message_edit
message_react
message_unreact
message_pin
message_unpin
user_profile_setname
user_profile_setemail
user_profile_sethandle
user_profiles_uploadphoto
admin_userpermission_change

The following are small functions that fetch information and return it. They are easiest to do once the structure has been finalised and no changes need to be made. These are the lowest priority functions as no other functions require them to be complete. We estimate that they should take no longer than a few hours to do collectively.

channel_details
channels_list
channels_listall
channel_messages
user_profile

The standup functions, while they are substantial, are not necessary to the above basic functions and have a lower priority, being a larger portion of work for a minor feature. Standup may take up to a day to complete.

standup_start
standup_send
## Design Smells
We attempted to cover as many design smells as possible during implementation. Towards the end of iteration 3, we met and went through our code to consider any design smells that weren’t considered during the initial implementation phase. We learned from iteration 2 that we needed to improve our commenting and communication within the code to make it clearer for each other and we took this into consideration.

# Rigidity (Tendency to be too difficult to change) & Fragility (Tendency for software to break when a single change is made)

Rigidity and fragility of our code mainly existed within our data structures. Most functions relied on a dictionary which stored a list of Class instances. For example, data[‘users’] contained a list of the User class, which contained fields such as u_id. Overall, we considered this to be generally unavoidable and as such we did not make any changes to the basic data structure without meeting and discussing in depth.

Elsewhere, our code was generally not rigid our fragile and we were each able to implement and update our functions without causing issues in other functions.

# Immobility ( Previous work is hard to reuse or move)

Generally, our code was easy to reuse since we considered our data structures first and then all implemented our functions around them. This allowed us to avoid the issue of having to drastically change our data which would have then likely caused a significant rewrite of many functions.

If there were changes that had to be made, they usually stemmed from bugs which went unnoticed or untested and thus our previous work only required small changes to work

# Viscosity (Changes feel very slow to implement)

When adding code, usually, any additions fit naturally into the backend without much trouble, without modifying the design significantly. We emphasised that functions should generally contain 50 lines of solid code, to ensure flexibility of adding new code to adjust the function.  

# Opacity (Difficult to understand)

From the start of implementation, we discussed the importance of strong intrinsic and internal documentation in producing readable and easy to understand code. We determined that this was very important for ourselves in understanding our own and our teammates’ code, to others reading our code, and, in theory, maintenance programmers in the future.

As a result, we all commented significant aspects of our code as we wrote it, and updated them as implementation progressed. We also ensured our indentation was correct and that spacing was appropriate in order to separate large code blocks into broad “categories”.

We also considered intrinsic documentation such as variable and function names to ensure their purpose was clear and camel case or underscores were used for readability. For example we wrote ‘getUserFromToken” as opposed to “getuser()”. Notably, in iteration 3 we changed some fields in our Classes to more accurately reflect their purpose.

Adding descriptions to our ValueErrors and AccessErrors also made for more understandable code, especially towards the end of iteration 3 where we would often debug others’ functions since we found the new perspective to be more useful in finding small errors.

# Needless complexity  (Things done more complex than they should be) 

We decided to make the functions as short and simple as possible (we referred to KISS).  We often use the simplest tools to solve a problem in the simplest way, for example, we used the regex tool in auth_login function as opposed to implementing our own complex solution.

In many files, the main function was kept as small and simple as possible through abstraction, where we used functions and spacing as we saw fit. The aforementioned global file was very important here as there were many calls from global which were used to clean up other files quite significantly.

Furthermore, we often considered various ways to implement functions by designing pseudocode and discussing which solved the problem most efficiently. For example, in channel/messages, our original implementation involved finding messages and appending them to a new data structure. After reviewing this, we created pseudocode for a new implementation which could simply find the correct index and return data within a range of the already existing data structure. This appeared more efficient to us and was then implemented into our final iteration’s code.

# Needless repetition ( Lack of unified structures)

We addressed the issue of needless repetition by creating a file which could be imported into every function where necessary. Originally, the file was designed to hold only data structures including our classes for User, Message etc., and our main dictionary, which contained a list of instances of each class. 

In Iteration 3, we realised that many functions would require repeated code. For example, identical code was needed to determine the user’s email and u_id from the token. Our first step was to create a “getUserFromToken” function in each file to address this. However, later we decided to add commonly used functions into the “global” file, hence addressing the needless repetition.

# Coupling  (Interdependence between components)

There were several functions that were relied on very heavily by the rest of the backend, such as auth_register and auth_login, and we relied on it to work so that we could write and test other functions. It was unavoidable that these sections would be coupled to such an extent and as these functions were fairly straightforward to write and test, we did not feel the need to significantly reduce the interdependency in our system.


## Functional Requirements

1. Login (Cathleen)
2. Logout (Baotran)
3. Create new account (Baotran)
4. delete account
5. User home page with image(user can see messages of users they follow)
6. Send message to followers 
7. View followers 
8. Follow User (Cathleen)
9. Search for User (Cathleen)
10. User Profile (Baotran)
11. Sending private messages
12. Edit Profile (Baotran)

## Non-functional Requirements

1. Only Support Google Chrome
2. Only support Desktop
3. Light and Dark Theme option (Baotran)
4. Secured log in

## Use Cases

1. Send message to followers (Baotran)
- **Pre-condition:** 
  1. User must be logged in
  2. User must be on the homepage

- **Trigger:** 
  User clicked on "post" button.

- **Primary Sequence:**
  1. System prompt user for message
  2. User types message
  3. User clicks "post"
  4. System posts message
  5. System refreshes home page (redirects user to the home page again) with new post shown

- **Primary Postconditions:** 
  1. User's message is posted if user entered valid input

- **Alternate Sequence:**
  1. User enters bad input (e.g., nothing, spaces)
  2. User clicks "post"
  3. System does not post message
  4. System refreshes home page (redirects user to the home page again)

2. View followers (Baotran)
- **Pre-condition:** 
  1. User must be logged in
  2. User must be on profile page

- **Trigger:** 
  User clicked on "followers" button

- **Primary Sequence:**
  1. User clicks on followers button
  2. System redirect user to follower page
  3. System displays list of followers
  
- **Primary Postconditions:**
  1. The user is on the followers page and user's followers are shown else "no followers" is displayed if user does not have followers.

- **Alternate Sequence:**
  1. User does not have followers
  2. User clicks on followers button
  3. System redirect user to followers page
  4. System displays "no followers"


3. Follow User (Cathleen)
- **Pre-condition:**
  1. User is logged in.

- **Trigger:**
  User clicked the "Follow" button on the intended user's profile. 

- **Primary Sequence:**
  1. User selects the intended user’s profile to view.
  2. System displays a “Follow” button on the intended user’s profile.
  3. User clicks on the “Follow” button.
  4. System displays a “Unfollow” button instead of a “Follow” button on the intended user’s profile.
  5. System adds 1 follower to the intended user’s followers list and adds 1 following to the user's following list.

- **Primary Postconditions:**
  1. User follows the intended user and intended user gains a follower.

- **Alternate Sequence:**
  1. The user is not logged in.
	a. When the user tries to follow the intended user, the system displays a message that gives the option to log in, or create a new account.
  2. The intended user's profile is deleted.
  a. When the user tries to follow the intended user and that profile is deleted, the user is unable to follow the intended user and the system displays a message that the user does not exist.
  3. The user tries to follow themselves.
  a. When the user tries to follow themselves, the system will redirect them.

4. Search for User (Cathleen)
- **Pre-condition:**
  1. User has website open.
  2. User is logged in.

- **Trigger:**
  User enters a username and/or name into the website's search bar.

- **Primary Sequence:**
  1. User selects the search bar. 
  2. User enters a username and/or name into the search bar.
  3. System searches for possible and similar users with username and/or name.
  4. System displays a list of possible user profiles.

- **Primary Postconditions:**
  1. System displays a list of possible user profiles from entered username/name.

- **Alternate Sequence:**
  1. User is not logged in.
  a. When the user tries to follow the intended user, the system displays a message that gives the option to log in, or create a new account.
  2. The system cannot find any possible user profiles.
	a. The system displays "no users found".

5. Send private message
- **Pre-condition:** 
  1. Must be logged in.
  2. Must be on a user's profile page.

- **Trigger:**  
  User clicks on "Message" button on the intended user's profile.	

- **Primary Sequence:**
  1. User click on another user's profile.
  2. System displays profile which has "Message" button.
  3. User clicks on "Message" button.
  4. System displays chat log between the two users and a text bar at the bottom.
  5. User types in the text bar and presses enter to send message.
  6. System displays the new message on the chat log for both users.

- **Primary Postconditions:** 
  The chat log for both users has been updated with the new message.

- **Alternate Sequence:**
  1. User is not logged on.
  2. User clicks "Message" button.
  3. Displays page to log in or create an account.

6.  Post an Image with Message (Kolby / sZeru)
- **Pre-condition:**
  1. Must be logged in.

- **Trigger:** 
  1. User must click an image button on the message field.

- **Primary Sequence:**
  1. A popup appears, asking the user to provide the path to the image on their computer.
  2. User enters a valid path.
  3. User presses 'add'. The image is appended to the buttom of their message field.
  4. The user types a message and presses 'post'.
  5. System posts message.

- **Primary Postconditions:**
  1. The image and message are posted.

- **Alternate Sequence:**
  1. User does not select a valid path, and presses 'add'.
  2. The path entry field is set to a red border. A prompt in red font displays "Invalid Path."
  3. The user can edit the path provided.

- **Alternate Sequence <optional>:** 
  1. User selects a valid path to an image that is too large.
  2. The path entry field is set to a red border. A prompt in red font displays "The image is too large."
  3. The user can edit the path provided.



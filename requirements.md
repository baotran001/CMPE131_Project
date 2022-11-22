## <remove all of the example text and notes in < > such as this one>

## Functional Requirements

1. Login
2. Logout
3. Create new account
4. delete account
5. User home page (user can see messages of users they follow)
6. Send message to followers
7. View followers
8. Follow User
9. Search for User
10. requirement
11. requirement
12. requirement

## Non-functional Requirements

1. non-functional
2. non-functional
3. non-functional
4. non-functional

## Use Cases

1. Send message to followers
- **Pre-condition:** 
  1. User must have written a message 
  2. User must be logged in

- **Trigger:** 
  User clicked on "post" button.

- **Primary Sequence:**
  
  1. System prompt user for message
  2. User types message
  3. User clicks "post"
  4. System posts message
  5. System refreshes home page

- **Primary Postconditions:** 
  1. User's message is posted

2. View followers
- **Pre-condition:** 
  1. User must be logged in
  2. User must be on profile page

- **Trigger:** 
  User clicked on "followers" button

- **Primary Sequence:**
  
  1. User clicks on followers button
  2. System redirect user to follower page
  
- **Primary Postconditions:**
  The user's follower are shown.

3. Follow User
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

4. Search for User
- **Pre-condition:**
  1. User has website open.

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
  1. The system cannot find any possible user profiles.
	a. The system displays "no users found".

5. Use Case Name (Should match functional requirement name)
- **Pre-condition:** <can be a list or short description> Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua.

- **Trigger:** <can be a list or short description> Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur. 

- **Primary Sequence:**
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Et sequi incidunt 
  3. Quis aute iure reprehenderit
  4. ... 
  5. ...
  6. ...
  7. ...
  8. ...
  9. ...
  10. <Try to stick to a max of 10 steps>

- **Primary Postconditions:** <can be a list or short description> 

- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Ut enim ad minim veniam, quis nostrum e
  3. ...

- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Ut enim ad minim veniam, quis nostrum e
  3. ...

6. Use Case Name (Should match functional requirement name)
- **Pre-condition:** <can be a list or short description> Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua.

- **Trigger:** <can be a list or short description> Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur. 

- **Primary Sequence:**
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Et sequi incidunt 
  3. Quis aute iure reprehenderit
  4. ... 
  5. ...
  6. ...
  7. ...
  8. ...
  9. ...
  10. <Try to stick to a max of 10 steps>

- **Primary Postconditions:** <can be a list or short description> 

- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Ut enim ad minim veniam, quis nostrum e
  3. ...

- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Ut enim ad minim veniam, quis nostrum e
  3. ...



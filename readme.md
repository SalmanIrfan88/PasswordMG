# CS50 Final Project - Password Manager

The project is a web Application and a password generator extension. where users can enter their login details about their accounts. It will help them to remember the details of their accounts to login whenever they need them to login urgently and the password manager and the extension itslef also generates a random password for the user to use (if he can't make one of his own OR needs a secure pass to use) if he needs it and the password given by this generator is very secure.No one can easily crack it and even they were able to crack it, it will take them very long to do that... 

Languages and Technologies used are:

- HTML5
- CSS3
- bootstrap
- javascript
- python 3
- sqlite3
- jinja 
- flask 
- json
- other small libraries or packages

## How the webpage works?

The idea is simple. The user can register ,login or logout easily.
 During registration user needs to enter these fields:

- Username : a username is only occupied by 1 user (2 users cannot use 1 username) in simple words (a username can only be used once).
- Password : password can be used as any keyword so the user can easily remember it, otherwise if the user lost this password he will lose his all other account's details.
- Confirmation : to confirm the given password (is that correct or not)... and is hashed after checks are done...

after registration user is directly logged in for the first time and ready to go to enter his details which he wants to get remembered by the password manager...

if user has already made an account he can directly login by clicking on login button.
During login/signin user needs to enter these fields:
- Username
- Password 
to log out just click on logout button once and it will log you out of the session.

## How the extension works?

it simply generates a strong random password when ever you need it and i thought it will be great to just have a password for you on your head.
it  is simple to use
you can copy it directly form theri 
its relevent, its secure and its fast.
for this you don't need to log in no registeration no nothing just open the extension and boom you have a password after one click Hence its super fast...

### Routing

Each route checks if the user is authenticated(logged in). It means if correct username and password were supplied. So for example another user cannot enter in any other's passwords. The same is for everyone. everyone can view only their information.

### Sessions

The webpage uses sessions to confirm that user is registered. Once the user logins, his credentials are checked. Once everything passes a session is created for the user to use.

### Database

Database stores all users, informations, login details submissions from the user. The tables, like user's submissions uses foreign keys to relate users main account. where his all login information is saved.

## Possible improvements

As all applications this one can also be improved. Possible improvements:

- have many kinds of user_interfaces to use this.
- whenever and where-ever user make a new account it should give a popup to directly save that given info of a newly registered account or a logged in one.
- it should have all details about the accounts those are given and saved are in this database like (when was a account is created and else)
- it should have a delete button, if user wants to delete his information so he can do (well i haven't included it purposely. which is if anyone else had access to the user's account he cant delete hi personal information or cannot remove any of his data). well it's not hard to impliment a button which deletes something....

## How to launch application

1. launch Cs50 version of vs code.io
2. you can run the flask app directly form terminal
3. Run command prompt in the folder and run `python -m flask run` or just open your browser and go to `http://127.0.0.1:5000/`
4. You are ready to go!



## How to launch chrome extention

1. launch Cs50 version of vs code.io
2. Clone the code of the generator extension or simply download it in any folder(after downloading just unzip the folder).
3. open chrome and locate to extensions .
4. then click on load unpacked .
5. then go to that directory where you downloaded the code form vs code.
6. now just click on top right corner on extension's icon and pin the logo on top of the extensions toolbar.
7. and there you have the working extension... You are ready to go!

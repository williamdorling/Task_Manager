#=====importing libraries===========

from datetime import date

#====Login Section====

# Pseudocode
# read user.txt
# create dictionary with keys as usernames, and values as passwords
# Prompt user to enter username
# validate if username exists
# prompt user to enter password
# check if password matches with the username

username_dictionary = {}
with open('user.txt','r+') as usernames:
    for line in usernames:
        username_password = line.strip('\n').split(', ')
        # returns list in form ['username', 'password']
        username_dictionary[username_password[0]] = username_password[1]
        # adds username/password combination to dictionary

username = input("Welcome! Please enter your username: ")
while username not in username_dictionary: # checks username is valid
    username = input("No user with this name, please enter a valid username: ")

password = input("Thank you, please enter your password: ")
while username_dictionary[username] != password: # checks password is correct
    password = input("Incorrect password, please enter your correct password: ")
print(f"\nThank you, {username}, you are successfully logged in\n")


while True:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
    if username == "admin":
        menu = input('''Select one of the following options:
    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks
    vs - view statistics
    e - exit
    : ''').lower()
    else:
        menu = input('''Select one of the following options:
    r - register a user
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit
    : ''').lower()

    if menu == 'r':
        if username != "admin":
            print("Only the admin may register a new user\n")
        else:
            new_username = input("Please choose a username: ")
            while new_username in username_dictionary:  #check username is not already taken
                new_username = input("This username is taken, please choose another username: ")
            new_password = input("Please enter a password: ")
            confirm_password = input("Please confirm your password: ")
            while new_password != confirm_password:  # check password matches confirmation
                new_password = input("Passwords do not match, please enter a password: ")
                confirm_password = input("Please confirm your password: ")
            with open('user.txt','a') as usernames:  # open user.txt to append new username password combination
                usernames.write(f"{new_username}, {new_password}\n")
                username_dictionary[new_username] = new_password
            print(f"\nThank you, user {new_username} created.\n")

    elif menu == 'a':
        task_username = input("Please enter the user whom this task will be assigned to: ")
        while task_username not in username_dictionary:  # check that chosen user exists 
            task_username = input(f"User {task_username} not found, please enter a valid username: ")
        title = input("Please enter a title of this task: ")
        description = input("Please enter a description for this task: ")
        due_date = input("Please enter the due date for this task: ")
        current_date = date.today()
        with open('tasks.txt','a') as tasks:  # open tasks.txt to append new task
            tasks.write(f"{task_username}, {title}, {description}, {current_date}, {due_date}, No\n")
        print(f"\nThank you, task {title} added for {task_username}.\n")

    elif menu == 'va':
        print("\nAll Tasks:")
        print("------------------")
        with open('tasks.txt', 'r+') as tasks:  # open tasks.txt to read tasks
            for line in tasks:
                [user, title, description, start_date, due_date, complete] = line.strip('\n').split(', ')
                print(f"Task: \t\t {title}")
                print(f"Assigned to: \t {user}")
                print(f"Date assigned: \t {start_date}")
                print(f"Due date: \t {due_date}")
                print(f"Task complete? \t {complete}")
                print(f"Task description: \n {description}")
                print("------------------")
        print("\n")

    elif menu == 'vm':
        print("\nMy Tasks:")
        print("------------------")
        with open('tasks.txt', 'r+') as tasks:
            for task in tasks:
                [user, title, description, start_date, due_date, complete] = task.strip('\n').split(', ')
                if user == username:  # select only tasks assigned to the logged-in user
                    print(f"Task: \t\t {title}")
                    print(f"Assigned to: \t {user}")
                    print(f"Date assigned: \t {start_date}")
                    print(f"Due date: \t {due_date}")
                    print(f"Task complete? \t {complete}")
                    print(f"Task description: \n {description}")
                    print("------------------")
        print("\n")

    elif menu == 'vs' and username == 'admin':  # check user is admin
        with open('tasks.txt', 'r+') as tasks:
            number_of_tasks = sum(1 for task in tasks)  # counts number of tasks by creating list of 1s and summing up
        with open('user.txt', 'r+') as users:
            number_of_users = sum(1 for user in users)  # counts number of users as above
        print("------------------")
        print(f"Number of users: {number_of_users}")
        print(f"Number of tasks: {number_of_tasks}")
        print("------------------")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again\n")
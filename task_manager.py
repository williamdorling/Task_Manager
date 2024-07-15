#=====importing libraries===========
'''This is the section where you will import libraries'''

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file
    - Use a while loop to validate your user name and password
'''
# read user.txt
# create dictionary with keys as usernames, and values as passwords
# Prompt user to enter username
# validate if username exists
# prompt user to enter password
# checks if password matches with the username

username_dictionary = {}
with open('user.txt','r+') as usernames:
    for line in usernames:
        username_password = line.strip('\n').split(', ')
        # returns list in form ['username', 'password']
        username_dictionary[username_password[0]] = username_password[1]
        # adds username/password combination to dictionary


username = input("Welcome! Please enter your username: ")
while username not in username_dictionary:
    username = input("No user with this name, please enter a valid username: ")

password = input("Thank you, please enter your password: ")
while username_dictionary[username] != password:
    password = input("Incorrect password, please enter your correct password: ")
print(f"Thank you, {username}, you are successfully logged in")



while True:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
    menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    if menu == 'r':
        '''This code block will add a new user to the user.txt file
        - You can use the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same
            - If they are the same, add them to the user.txt file,
              otherwise present a relevant message'''
        new_username = input("Please choose a username: ")
        while new_username in username_dictionary:
            new_username = input("This username is taken, please choose another username: ")
        new_password = input("Please enter a password: ")
        confirm_password = input("Please confirm your password: ")
        while new_password != confirm_password:
            new_password = input("Passwords do not match, please enter a password: ")
            confirm_password = input("Please confirm your password: ")
        with open('user.txt','a') as usernames:
            usernames.write(f"{new_username}, {new_password}\n")
            username_dictionary[new_username] = new_password
        print(f"\nThank you, user {new_username} created.\n")

    elif menu == 'a':
        pass
        '''This code block will allow a user to add a new task to task.txt file
        - You can use these steps:
            - Prompt a user for the following: 
                - the username of the person whom the task is assigned to,
                - the title of the task,
                - the description of the task, and 
                - the due date of the task.
            - Then, get the current date.
            - Add the data to the file task.txt
            - Remember to include 'No' to indicate that the task is not complete.'''

    elif menu == 'va':
        pass
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in the PDF
            - It is much easier to read a file using a for loop.'''

    elif menu == 'vm':
        pass
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the 
              username you have read from the file.
            - If they are the same you print the task in the format of Output 2
              shown in the PDF '''

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")
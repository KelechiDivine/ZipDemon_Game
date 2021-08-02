# email= input("Enter your email: ").strip()
# user_name= email[:email.index('@')]
# domain= email[email.index('@') + 1]
#
# name_placeholder = 'Your user name is {}'.format(user_name) + ' & domain is ' + '{}'.format(domain)
# print(name_placeholder)


"""A more pythonical way of doing this is by using a function"""

def email_slicer(emails):
    username, _, domain= emails.strip().partition("@")
    return 'Your user name is {}'.format(username) + ' & domain is ' + '{}'.format(domain)
# user_input= input("Enter your name here: ")
# print(email_slicer(user_input))

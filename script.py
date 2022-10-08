import re

def isValidMail(mail):
    # Regex for mail structure validation
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(regex, mail)):
        return True
    else:
        return False

mail = input("Enter your mail id: ")

if isValidMail(mail):
    username = mail[0:mail.index('@')]
    domain = mail[mail.index('@') + 1:]
    print("Username: ", username)
    print("Domain: ", domain)
else:
    print("Invalid Mail !")
# Voting Program
# Coded by xMistx

import time

# Subroutine (1)

# Username Variable
Username = str(input("Please enter your username: "))

# Age Variable
Age = int(input("Please enter your age: "))

# Telephone Variable
Telephone = str(input("Please enter your telephone number: "))

#this person a woman?!?!?!?!?!?1/1/1/?!?!?1/1/11/1/?!?!
isWoman = bool(input("Yo you a woman?: "))

# Vote Variable
def Vote1():
    Eligibility = False
if Age >= 18 and !isWoman:
    print('Checking the UK Voting Database..')
    # Program will sleep for 5 seconds
    time.sleep(5)

    # Prints out if elegibility + information
    print('-------------------------')
    print('<!> Vote Eligibility Check <!>')
    print(' ')
    print(' Username: ' + Username)
    print(' Age: ', Age)
    print(' Telephone: ' + Telephone)
    print(' ')
    print(' You are eligible!')
    print(' Please head over to https://www.gov.uk/how-to-vote ')
    print('-------------------------')

else:
    print('Checking the UK Voting Database..')
     # Program will sleep for 1 second
    time.sleep(5)
    # Prints out if elegibility + information
    print('-------------------------')
    print('<!> Vote Eligibility Check <!>')
    print(' ')
    print(' Username: ' + Username)
    print(' Age: ', Age)
    print(' Telephone: ' + Telephone)
    print(' ')
    print('   You are NOT eligible to Vote because you are a woman!')
    print('-------------------------')

# Main Program
Vote1()

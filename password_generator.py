# import random library to use for generating the random password
import random
# all alpha numeric characters used in making of the password generator
characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*()?.,0123456789'
# since many people use different platforms, it's always a good idea to have a different password
# for each platform (one for facebook, one for instagram, etc.) so the user can choose here
# and pick how many platforms or passwords
number = input('Please enter how many passwords you want: ')
# In java we have try-catch but in Python we have try-except
# first try is for a number that the user will enter, and checks whether the input is a number or not
try:
    number = int(number)
# except is for the error case
except:
    print("Please enter a number")
# the user will pick how long and complex there password is
length = input('Length of password: ')
# try-except for length and must be a number
try:
    length = int(length)
except:
    print("Please enter a number")
print('\nGenerated Passwords for each Platform:')
# Pass generator using nested loop
for pwd in range(number):
  password = ''
  for i in range(length):
    password += random.choice(characters)
  print(password)
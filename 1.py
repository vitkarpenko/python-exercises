from datetime import datetime


name = input('Please enter your name: ')
age = int(input('Please enter your age: '))
times = int(input('How many times do you want me to print the message: '))

message = '\n{}, you will turn 100 years old in {}'.format(name, datetime.now().year - age + 100)

print(message * times)

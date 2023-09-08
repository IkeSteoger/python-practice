# This program says hello and asks for a name.

print('Hello, world!')
print('What is your name?')    # ask for their name
yourName = input()
print('It is good to meet you, ' + yourName)
print('The length of your name is:')
print(len(yourName))
print('What is your age?')    # ask for their age
yourAge = input()
print('You will be ' + str(int(yourAge) + 1) + ' in a year.')
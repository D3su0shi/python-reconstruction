# this is just a code that asks for name
'''
def hello() :
    print('Hello, whats ur name?')


hello()
usrName = input('Enter name: ')

print("oh ur name is " + usrName)
print('thats a pretty dumb name with only ' + str(len(usrName)) + ' letters')

usrAge = int(input('how old are you type shi? '))
if usrAge < 18 : 
    print('ur less than 18')
else:
    print('old')

'''
#--------
'''
# This is a guess the number game.

import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
 print('Take a guess.')
 guess = int(input())
 if guess < secretNumber:
    print('Your guess is too low.')
 elif guess > secretNumber:
    print('Your guess is too high.')
 else:
    break # This condition is the correct guess!
if guess == secretNumber:
 print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
 print('Nope. The number I was thinking of was ' + str(secretNumber))


'''
def collatz(number) : 
    try :
        if number % 2 == 0 : # checks if the number is even
            evenSub = number // 2
            print(evenSub)
            return int(evenSub)
        elif number % 2 == 1 : # checks if the number is odd
            oddsub = 3 * number + 1
            print(oddsub)
            return oddsub
    except ValueError :
        print('Thats a string')
    
usrNum = int(input("Enter a number : "))
newNum = usrNum


while newNum != 1:
    newNum = collatz(newNum)


'''
    this was old code :

    newNum = usrNum

    while collatz(newNum) != 1:
        newNum = collatz(usrNum)

    after going through it at first the output kept shifting and it was an infinite loop . i saw what i did was wrong 
    because i was calling the function in the beginning wrongly. the collatz(newNum) != 1 will alwaybe be true and hence
    and infinite loop. After solving that problem a new issue that arose was that i kept changing newNum to the value 
    returned by the collatz of the usrNum and not the newNum so that kept pasting the same value. at the end i saw two possible
    solutions. one where i remove entirely the newNum because its a bit reduntant but as it is a usr input number we might want
    to use it somewhere else so ill keep the use of the newNum

'''

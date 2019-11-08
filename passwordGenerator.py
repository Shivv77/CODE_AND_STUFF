

import string
import random


def bigTex(passLength):
    # return a charecter fro  a defined string

    charecters = string.ascii_letters + string.digits + string.punctuation
    password = ''

    for i in range(passLength):
        randomNumber = random.randint(0, len(charecters)-1)
        password += charecters[randomNumber]

    return password


'''
def main():
    
    for i in range(100):
       print(bigTex())
        

main()
'''


def main():

    userInput = int(input("enter password lenght: "))
    howMany = int(input('how many??: '))
    pwFile = open('passwords.txt', 'w')
    for i in range(howMany):
        password = bigTex(userInput)
        print(password)
        pwFile.write(password + '\n')

    pwFile.close()


main()

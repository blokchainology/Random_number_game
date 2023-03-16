import random as rd

number = rd.randrange(0 , 124)
print('\n help: number is between 0 to 124 \n')

while True :
    userSendNumber = input('Enter number: ')
    userSendNumber = int(userSendNumber)
    if userSendNumber == number :
        print(f'\n Ok ! number is {number} :)\n')
        break
    elif userSendNumber < number :
        print('it is number bigger than your number Try agian')
    else:
        print('it is number smaller than your number Try agian')

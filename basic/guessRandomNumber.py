'''
simple guess number using opp 
'''


import random as rd


# class number 
class Number:
    #get number for input
    def getNumber(*args):
        number = int(input("Enter a number : "))
        return number

    #generate random number using radom
    def generateRandomNumber(*args):
        a= 0; b = 0
        print(f'interval(integer)')
        print("Limit \n")
        isInteger = False
        while isInteger == False:
            try :
                a = int(input("a = "))
                b = int(input("b = "))
                isInteger = True
            except ValueError:
                print(f"please input integer")
        return rd.randint(a,b)


    





#how to code work
number = Number()
randomNumber = number.generateRandomNumber()
isTrue = False  

'''
if input number and random number is equal, break. else give input number more
'''
while True:
    numberInput = number.getNumber()
    if randomNumber == numberInput : 
        print(f"the number is {numberInput}")
        break 

    print(f'{numberInput} wrong \n')
  

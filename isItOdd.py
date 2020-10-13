class IsitOdd:
    #init a variabel number
    def __init__(self):
        self.number = int(input("Enter a number : "))


    #check odd number
    '''
    if number modulus 2 equal 0 , number is even. else odd
    '''
    def checkOdd(self):
        if self.number%2 == 0:
            return f"{self.number} is even"

        else:
            return f"{self.number} is odd"


#excute
isitodd = IsitOdd()
print(isitodd.checkOdd())        

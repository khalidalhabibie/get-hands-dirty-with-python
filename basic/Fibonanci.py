#ask many terms
nterms = int(input("How many terms? "))

# one, two term and count 
n1, n2, count  = 0, 1, 0



# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1


#print total 
print(f'total = {nth}')
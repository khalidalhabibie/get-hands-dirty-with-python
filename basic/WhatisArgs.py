'''
simple way how to using arg


how to run it
example:
python WhatisArgs.py 1 6 
or
python3 WhatisArgs.py 1 6 



'''


#import sys
import sys
from sys import argv

#define variabel 
element1  = int(sys.argv[1])
element2 = int(sys.argv[2])

#add arg for result
add = element1 + element2

#show output
print(f'list of argument {sys.argv}')
print(f'Result {add}')



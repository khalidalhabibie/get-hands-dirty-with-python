'''
difference between continue and break
'''


#how to using break
print("break if i equal 5 :")
for i in range(10):
    if i == 5:
        break

    else:
        print(i)

'''
output : 

break if i equal 5 :
0
1
2
3
4
'''

#how to using continue
print("continue if i equal 5 :")
for i in range(10):
    if i == 5:
        continue

    else:
        print(i)


'''
output:
continue if i equal 5 :
0
1
2
3
4
6
7
8
9
'''


'''
note : continue just bypass once loop and break stop loop

'''
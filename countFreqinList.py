def count_elemnt(my_list):
    freq = {} 
    for item in my_list: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
    return freq


#data input
my_list = [2, 2, 5, 1, 2, 3, 5, 1, 2, 7]

#call count_elemnt for freq variabel
freq = count_elemnt(my_list)

#output 
for key, value in sorted(freq.items()): 
    print(f"{key} ada {value}")


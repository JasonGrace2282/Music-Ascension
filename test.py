counter = 0
my_list = [0]
for i in my_list:
    print(i)
    my_list.append(i)
    counter+=1
    if counter == 10000:
        exit(0)
#Code to sort a given list

list = [6,2,8,1,10]

temp = 0

for i in range(len(list)):
    for j in range(len(list)-1):
        if list[j] > list[j+1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp

print(list)
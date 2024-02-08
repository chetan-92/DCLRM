#Code to find max and min value/elements in a given list

def max_min_element(lst):
    return max(lst),min(lst)

list = [5,3,87,100,10,6]
a,b = max_min_element(list)
print("max element in the list is " + str(a))
print("min element in the list is " + str(b))

print("max and min element in the list is " + str(max_min_element(list)))


def max_element2(lst):
    max_element = lst[0]
    for num in lst[1:]:
        if num > max_element:
            max_element = num
    return max_element

list = [500,300,87,100,10,6]
max_element = max_element2(list)

print("max element in the list is " + str(max_element2(list)))

def min_element2(lst):
    min_element = lst[0]
    for num in lst[1:]:
        if num < min_element:
            min_element = num
    return min_element

list = [500,300,87,100,1,6]
min_element = min_element2(list)

print("min element in the list is " + str(min_element2(list)))
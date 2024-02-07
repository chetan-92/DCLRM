# case 1 using the sum function of python
def add_elements_of_list(lst):
    return sum(lst)

# test the function
numbers = [1,2,3]
print(add_elements_of_list(numbers))


# case 2 without using the sum function of python
def add_elements_of_list2(lst):
    total = 0
    for element in lst:
        total += element
    return total


# test the function
numbers = [1, 2, 3]
print(add_elements_of_list2(numbers))

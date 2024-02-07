# case to multiply elements of list
def multiply_elements_of_list(lst):
    total = 1
    for element in lst:
        total *= element
    return total


# test the function
numbers = [1, 2, 3, 4]
print("multiplication of all given elements is " + str(multiply_elements_of_list(numbers)))

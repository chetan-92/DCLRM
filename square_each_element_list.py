# case to square each element of the list
def square_elements_of_list(lst):
    result = []
    for element in lst:
        result.append(element ** 2)
    return result


# test the function
numbers = [1, 2, 3, 4]
print("new output squared elements list is " + str(square_elements_of_list(numbers)))

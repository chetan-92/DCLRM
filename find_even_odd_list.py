#Code to find the even and odd numbers in a given list
#code to chcek if a given single value is even or odd
a = 12

if a%2 == 0:
    print("even")
else:
    print("odd")


#code to check if the given list has all even or all odd or mixed values

def check_even_odd(lst):
    has_even = False
    has_odd = False

    for element in lst:
        if element%2 == 0:
            has_even = True
        else:
            has_odd = True

    if has_even and has_odd:
        return "Mixed"
    elif has_even:
        return "even"
    else:
        return "odd"

# Example usage:
my_list1 = [2, 4, 6, 8]
my_list2 = [1, 3, 5, 7]
my_list3 = [2, 3, 4, 5]

print("List 1:", check_even_odd(my_list1))
print("List 2:", check_even_odd(my_list2))
print("List 3:", check_even_odd(my_list3))
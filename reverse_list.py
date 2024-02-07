#code to reverse the elements index in the given list

def reverse_list(lst):
    return(lst[::-1])  #using inbuilt python function

numbers = [1,2,3,4,5]
print("new reversed list is " + str(reverse_list(numbers)))

def reverse_list2(lst):
    reversed_list = []    #using looping and not using inbuilt python function
    for i in range(len(lst)-1,-1,-1):
        reversed_list.append(lst[i])
    return reversed_list

numbers2 = [1,2,3,4,5,6]
print("new reversed list is " + str(reverse_list2(numbers2)))

def reverse_string(s):
    reversed_string = ""   #reversing a string instead of list.
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string

text = "chetan"
print("new reversed string is " + str(reverse_string(text)))
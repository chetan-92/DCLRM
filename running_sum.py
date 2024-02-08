#Code to find the sum of all previous and current element in the given list
def running_sum(lst):
    total = 0
    new_list = []
    for element in lst:
        total += element
        new_list.append(total)
    return(new_list)

my_list = [3,2,1,4,5]
print("running sum list is " + str(running_sum(my_list)))
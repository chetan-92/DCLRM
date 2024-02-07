# code to find the common element between the given lists

list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]

common_elements = []
#iterating each element from list1
for element1 in list1:
	#iterating each element from list2 against each element in list1
	for element2 in list2:
		#if the element from the fist list is equal to the element from second list
		if element1 == element2:
			#append the matching element into the new list
			common_elements.append(element1)

print(common_elements)

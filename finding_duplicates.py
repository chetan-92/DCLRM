def finding_duplicate(lst):
    for i in range(0,len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst[i] == lst[j]:
                return True
            else:
                pass
    return False


list = [1,1,1,3,3,4,3,2,4,2]
list2 = [1,2,3,4]

print(finding_duplicate(list))

# or code 2 where we can use length of the list and inbuilt set function to remove duplicates.
if len(set(list2)) != len(list2):
    print(True)
else:
    print(False)


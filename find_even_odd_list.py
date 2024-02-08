#Code to find the even and odd numbers in a given list

cif_list = [['a','A',1],['b','B',2]]

for element in cif_list:
    filename = '%s_%s_%s.csv' %(element[0],element[1],element[2])
    print(filename)


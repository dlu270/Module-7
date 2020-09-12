# Daniel Lu
# 9/12/20

# This function finds the unique elements of a list and prints them.

list1 = [1, 3, 3, 3, 6, 2, 3, 5]

def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    for x in unique_list:
        print (x)
        
print ("The unique elements of the list are: ")
unique(list1)

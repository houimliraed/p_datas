mySet = {'10','4','60'}
# you can only access the element in the set in a loop only
for element in mySet:
    print(element)
# sets has its own built in function , we can use add to add an element to the set
mySet.add('66')
print(mySet)
mySet.remove('10')
#remove only removes the first occurence of the element
print(mySet)
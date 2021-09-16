a=set()
# print(type(a))
a.add(5)
a.add(2)
a.add(6)
a.add(8)
# a.add([6,7,8])  cannot add a list
# a.add({4:500})  cannot add a dictonery
a.add((6,7,9,3))  #but can a touple in a set
# print(a)

# len method
# print(len(a))

#remove method
a.remove(5)
# print(a)

# pop method (it picks any random numbver from the set)
# print(a.pop())

#a.clear() empties the set

# union & intersection
b={2,5,6,7,8,0}
print(a.union(b))
print(a.intersection(b))

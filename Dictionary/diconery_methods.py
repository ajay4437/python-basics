mydict={
    "ajay": 'good boy',
    "fast": 'a quick manner',
    "marks": [1,3,4,6],
    "anotherdict": {'ajay': 'coder'},
    1:2
}
#print(mydict.keys())#keys of dictonery
#print(list(mydict.keys()))#print the keys of dictonery in the list formet
#print(list(mydict.values()))#print the values of dictonery in the list formet
#print(mydict.items()) #print the (key, value) of all contents of the dictonery
#print(mydict)

#update method
updatedict={
    'lovieh':'friend',
    'dinesh':'friend'
}
mydict.update(updatedict)
print(mydict)

#get method
print(mydict.get('ajay'))
#print(mydict['ajay1'])

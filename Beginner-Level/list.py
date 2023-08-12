
list = ['car','bike',30,40.01,50,True]
print(list)
print(len(list),type(list))

print(list[2:5]) #30,40,50
print(list[:5])#'car','bike',30,40,50
print(list[2:]) #30,40,50, True
list.insert(3,'Orange')
print(list)
list.append('0.2125415')
list.remove('0.2125415')
print(list)
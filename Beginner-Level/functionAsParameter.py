
list = ['car','bus','bike','jet']

def transport(x):
    print (x*3)

#transport(list) 
def map_simple(crazy,list):
       for items in list:
           crazy(items)
     
#map_simple(transport,list)
fruits = ['apple','banana','cherry']
def my_function(food):
    for x in food:
        print(x)
        
#my_function(fruits)

def my_function(x):
    return 5*x
print(my_function(3))
print(my_function(5))
print(my_function(9))
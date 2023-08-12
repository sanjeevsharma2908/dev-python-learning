
# class Human:
#     x = 5

# obj1 = Human()
# print(obj1.x)   
class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
     
     
    def methods(self):
        print("Hi, My name is " + self.name + " and I am " + self.age + " years old")        
   
   
        
h1 = Human("sanjeev_sharma","29")

h1.methods()
del h1
# here we have deleted h1
h1.name = "Sanjit Sharma"
h1.age = 29
h1.method()
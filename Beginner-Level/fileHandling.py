
import os
#reading the file
#f = open("Beginner-Level/info.txt", "r")
# print(f.readline())
# #print(f.read())
# #character wise reading
# print(f.readline())
# print(f.readline(5))

# for i in f:
#     print(i)

#Append Mode
# f = open("Beginner-Level/info.txt", "a")
# f.write('A nwe line is added')
    
# f.close()    
# f = open("Beginner-Level/info.txt", "r")
# print(f.read())
# f.close()


#Writing to the file

# f = open("Beginner-Level/info.txt", "w")
# f.write("A new line is added")
# f.close()

# f = open("Beginner-Level/info.txt", "r")
# print(f.read())

# creating a new file

#f = open("Beginner-Level/info1.txt", "x")
#f = open("Beginner-Level/info2.txt", "w")
# # even opening a file with 'w' mode is is doesn't exist it will be created


# Deleting  a file 
os.remove("Beginner-Level/info.txt")

# if os.path.exists("Beginner-Level/info2.txt"):
#     os.remove("Beginner-Level/info2.txt")
# else:
#     print('File Does Not Exist')


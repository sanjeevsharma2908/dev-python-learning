import random
def GenerateRandom(upper):
    r = random.randint(1,upper)
    return r

def main():
    program = True
    num1 = GenerateRandom(10)
    num2 = GenerateRandom(10)
    result = num1*num2
    while program:
        ans = input("what is  "+str(num1) + " x " + str(num2) + " = ")
        
        if ans.isdigit():
            if int(ans)==result:
                print("Correct Answer")
                program = False
            else:
                print("Incorrect Answer")
        else:
            print("Answer must be a Positive Integer")


x = 10
for i in range(x):
    main()                    
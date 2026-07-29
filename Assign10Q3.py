
def Factorial(No1):
    Fact = 1

    for i in range(1,No1+1):
        Fact =  Fact * i
     
    return Fact

def main():
    print("Enter the number : ")
    Num = int(input())

    ret = Factorial(Num)
    print("Factorial of given number is  : ",ret)
    
if __name__ == "__main__":
    main()
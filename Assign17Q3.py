#Factorial
def Factorial(No):
    Fact = 1

    for i in range(1,No+1,1):
        Fact = i * Fact

    return Fact

def main():
    print("Enter the number : ")
    Num = int(input())

    Ret = Factorial(Num)
    print("Factorial of the number is : ",Ret)
if __name__ =="__main__":
    main()
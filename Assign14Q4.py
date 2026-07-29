SmallNumber = lambda No1,No2 : No1 if No1 < No2 else No2   # we can also use if else statement in lambda function to find the smallest number between two numbers.
def main():
    print("Enter the number : ")
    Num1 = int(input())
    print("Enter the number : ")
    Num2 = int(input())

    Ret = SmallNumber(Num1,Num2)
    print("Minimum  number is : ",Ret)

if __name__ == "__main__":
    main()
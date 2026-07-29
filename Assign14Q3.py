LargeNumber = lambda No1,No2 : No1 if No1 > No2 else No2   # we can also use if else statement in lambda function to find the largest number between two numbers.
def main():
    print("Enter the number : ")
    Num1 = int(input())
    print("Enter the number : ")
    Num2 = int(input())

    Ret = LargeNumber(Num1,Num2)
    print("largest number is : ",Ret)

if __name__ == "__main__":
    main()
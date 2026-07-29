FindLargest = lambda Val1,Val2,Val3 : Val2 if ((Val2 > Val1) and (Val2 > Val3))   else Val3 if (Val3 > Val1) and (Val3 > Val2) else Val1
128
def main():
    print("enter the first number : ")
    Num1 = int(input())
    print("enter the second number : ")
    Num2 = int(input())
    print("enter the third number : ")
    Num3 = int(input())

    Ret = FindLargest(Num1,Num2,Num3)
    
    if Ret == Num1:
        print("The largest number is : ", Num1)
    elif Ret == Num2:
        print("The largest number is : ", Num2) 
    else:
        print("The largest number is : ", Num3)


if __name__ == "__main__":
    main()
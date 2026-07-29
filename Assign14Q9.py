Multiplication = lambda Val1,Val2 : Val1 * Val2

def main():
    print("enter the first number : ")
    Num1 = int(input())
    print("enter the second number : ")
    Num2 = int(input())

    Ret = Multiplication(Num1,Num2)

    print("Multiplication is : ",Ret)
if __name__ == "__main__":
    main()
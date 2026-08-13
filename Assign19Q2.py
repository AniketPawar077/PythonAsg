Multi = lambda Val1,Val2 :  Val1 * Val2 

def  main():
    print("Enter the first number : ")
    Num1 = int(input())

    print("Enter the second  number : ")
    Num2 = int(input())

    Ret = Multi(Num1,Num2)

    print("Multiplication of both  numbers is : ",Ret)
if __name__ == "__main__":
    main()
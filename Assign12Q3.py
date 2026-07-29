def ShowResult(No1,No2):
    
    Add = No1 + No2
    print("Additiion : ",Add)

    Sub = No1 - No2 
    print("Subtraction : ",Sub)

    Multi = No1 * No2
    print("Multiplication : ",Multi)

    Div = No1 / No2
    print("Division is : ",Div)


def main():
    print("Enter the first number : ")
    Num1 = int(input())

    print("Enter the second number : ")
    Num2 = int(input())
    ShowResult(Num1,Num2)

if __name__  == "__main__":
    main()
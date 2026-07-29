def CalculateSquare(No1):
    Sqr = No1 * No1

    return Sqr
    
def main():
    print("Enter the number : ")
    Num1 = int(input())

    Ret = CalculateSquare(Num1)

    print(Num1," Square is : ",Ret)
         
if __name__ == "__main__":
    main()
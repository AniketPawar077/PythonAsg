SquareNumber = lambda No : No * No

def main():
    print("Enter the number : ")
    Num = int(input())

    Ret = SquareNumber(Num)
    print("Square of number is : ",Ret)

if __name__ == "__main__":
    main()
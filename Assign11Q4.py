def ReverseDisplay(No):
    Reverse = 0
    Digit = 0

    while(No != 0):
        Digit = No % 10

        Reverse = Reverse * 10 + Digit

        No = No // 10

    return Reverse

def main():
    print("Enter the number  : ")
    Num = int(input())

    Ret = ReverseDisplay(Num)

    print("Reversed number is : ",Ret)
if __name__ == "__main__":
    main()
Divisibility = lambda Num : True if ((Num % 3 == 0) and (Num % 5 == 0) )else False

def main():
    print("Enter the size of list  : ")
    Num = int(input())

    Data = []

    for i in range(0,Num,1):
        print("enter the numbers : ")
        Value = int(input())
        Data.append(Value)

    Fdata = list(filter(Divisibility,Data))

    print("Numbers divisibl by 3 and 5 are : ",Fdata)

if __name__ == "__main__":
    main()
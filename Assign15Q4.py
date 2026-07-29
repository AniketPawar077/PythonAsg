from functools import reduce
Addition = lambda Num1, Num2 : Num1 + Num2

def main():
    print("Enter the number of elements : ")
    No = int(input())

    Data = []
    for i in range(0, No, 1):
        print("Enter the number : ")
        Num = int(input())
        Data.append(Num)


    RData = reduce(Addition, Data)
    print("Data after applying addition function is : ", RData)

if __name__ == "__main__":
    main()
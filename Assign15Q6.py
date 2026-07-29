from functools import reduce
Minimum = lambda Num1, Num2 : Num1 if Num1 < Num2 else Num2

def main():
    print("Enter the number of elements : ")
    No = int(input())

    Data = []
    for i in range(0, No, 1):
        print("Enter the number : ")
        Num = int(input())
        Data.append(Num)


    RData = reduce(Minimum, Data)
    print("Data after applying minimum  function is : ", RData)

if __name__ == "__main__":
    main()
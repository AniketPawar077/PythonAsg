Even = lambda No : No % 2 == 0 
def main():
    Count = 0
    print("Enter the number of elements : ")
    No = int(input())

    Data = []
    for i in range(0, No, 1):
        print("Enter the number : ")
        Num = int(input())
        Data.append(Num)


    FData = list(filter(Even, Data))
    print("Data after applying even function is : ", FData)

    for i in FData:
        Count = Count + 1

    print("count of Even numbers in Filter : ", Count)
if __name__ == "__main__":
    main()

Even = lambda Num: Num % 2 == 0

def main():
    
    Data = []

    for i in range(0, 5, 1):
        print("Enter the number : ")
        Num = int(input())
        Data.append(Num)

    Fdata = list(filter(Even, Data))
    print("Data after applying even filter function is : ", Fdata)


if __name__ == "__main__":
    main()
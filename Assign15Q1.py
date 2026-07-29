
Square = lambda Num: Num * Num

def main():
    
    Data = []

    for i in range(0, 5, 1):
        print("Enter the number : ")
        Num = int(input())
        Data.append(Num)

    Fdata = list(map(Square, Data))
    print("Data after applying map function is : ", Fdata)


if __name__ == "__main__":
    main()
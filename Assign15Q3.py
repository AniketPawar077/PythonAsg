
Odd = lambda Num: Num % 2 == 1

def main():
    
    Data = []

    for i in range(0, 5, 1):
        print("Enter the number : ")
        Num = int(input())
        Data.append(Num)

    Fdata = list(filter(Odd, Data))
    print("Data after applying odd filter function is : ", Fdata)


if __name__ == "__main__":
    main()
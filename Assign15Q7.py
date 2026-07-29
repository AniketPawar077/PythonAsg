StringLength5 = lambda String : String if len(String) > 5 else None

def main():
    print("Enter the number of strings : ")
    No = int(input())

    Data = []
    for i in range(0, No, 1):
        print("Enter the string : ")
        Num = input()
        Data.append(Num)


    SData = list(filter(StringLength5, Data))
    print("Strings with length greater than 5 are : ", SData)

if __name__ == "__main__":
    main()
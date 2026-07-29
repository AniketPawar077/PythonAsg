CheckEven = lambda No : No % 2 == 1   
def main():
    print("Enter the number : ")
    Num  = int(input())

    Ret = CheckEven(Num)

    if Ret == True:
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()
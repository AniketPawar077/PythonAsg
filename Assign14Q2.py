CubeNumber = lambda No : No * No * No

def main():
    print("Enter the number : ")
    Num = int(input())

    Ret = CubeNumber(Num)
    print("Cube of number is : ",Ret)

if __name__ == "__main__":
    main()
#Factorial
def PrimeNo(No):
    Add = 0
    iCount = 0
    for i in range(1,No+1,1):
        if No % i == 0:
            iCount = iCount +1

    return iCount

def main():
    print("Enter the number : ")
    Num = int(input())

    Ret = PrimeNo(Num)

    if Ret > 2:
     print("It is not a prime number ")
    elif Ret == 2:
        print("It is prime number")
    else:
        print("Invalid input")
if __name__ =="__main__":
    main()
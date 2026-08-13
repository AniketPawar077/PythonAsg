from MarvellouosNum import ChkPrime

def main():
    Data = []
    Size = 0

    print("Enter the Size of list : ")
    Size = int(input())

    for i in range(1,Size+1,1):
        print("Enter the list elements : ")
        i = int(input())
        Data.append(i)
        

    Ret = ChkPrime(Data,Size)

    print("Sum of prime nos : ",Ret)
if __name__ == "__main__":
    main()
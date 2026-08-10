#Factorial
def FactorAdd(No):
    Add = 0

    for i in range(1,No,1):
        if No % i == 0:
            Add = Add + i

    return Add

def main():
    print("Enter the number : ")
    Num = int(input())

    Ret = FactorAdd(Num)
    print("Addition  of the factors of given number  is : ",Ret)
if __name__ =="__main__":
    main()
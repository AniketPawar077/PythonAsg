def CheckDivisibility(No1):
    if No1 % 3 == 0 and No1 % 5 == 0 :
        return True
    else :
        return False
    
def main():
    print("Enter the  number : ")
    Num1 = int(input())

    Ret = CheckDivisibility(Num1)

    if Ret == True:
        print(Num1," is Divisible by 3 and 5")
    else:
        print(Num1," is not Divisible by 3 and 5 ")
         
if __name__ == "__main__":
    main()
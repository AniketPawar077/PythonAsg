def CheckGreater(No1,No2):
    if No1 > No2 :
        return True
    else :
        return False
    
def main():
    print("Enter the first number : ")
    Num1 = int(input())

    print("Enter the second number  : ")
    Num2 = int(input())

    Ret = CheckGreater(Num1,Num2)

    if Ret == True:
        print(Num1," is Greater ")
    else :
        print(Num2," is greater ")
         
if __name__ == "__main__":
    main()
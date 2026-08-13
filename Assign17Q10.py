def DigitAddition(Val):
    iDigit = 0
    i = Val
    iSum = 0

    while i != 0:
        iDigit = i % 10    
        i  = i // 10
        iSum = iSum + iDigit   
    
    return iSum

        
def main():
    print("Enter the number : ")
    Num = int(input())

    ret = DigitAddition(Num)
    print("Total no. of digits Addition in number present is : ",ret)
if __name__ =="__main__":
    main()
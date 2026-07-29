def SumDigitgs(No):
    Count = 0
    Factor = 0
    iSum = 0
    while No != 0 :
        
        Factor = No % 10        
        No = No // 10       # // used as floor division operator to get the quotient
        
        Count = Count+1

        iSum = iSum + Factor

    return iSum    

    
        

def main():

    print("Enter the number : ")
    Num = int(input())

    Ret = SumDigitgs(Num)

    print("Sum of digits in a number is : ",Ret)

if __name__ == "__main__":
    main()
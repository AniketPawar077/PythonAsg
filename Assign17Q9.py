def NumberCounter(Val):
    iDigit = 0
    i = Val
    iCount = 0

    while i != 0:
        iDigit = Val % 10    
        i  = i // 10
        print(i)
        iCount = iCount + 1  

    return iCount

        
def main():
    print("Enter the number : ")
    Num = int(input())

    ret = NumberCounter(Num)
    print("Total no. of digits in number present is : ",ret)
if __name__ =="__main__":
    main()
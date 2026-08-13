def ListElementFrequency(List1,Length,Snum):
    iCount = 0
    for i in range(Length):
     if List1[i] == Snum:
        iCount = iCount + 1
        
    return iCount
            
            
def main():
    Data1 = []
    print("Enter the List Size : ")
    Size = int(input())

    for i in range(1,Size+1,1):
        print("Enter the list elements : ")
        Values = int(input())
        Data1.append(Values)

    print("Enter the Number that we have to find  : ")
    SNum = int(input())

    Ret = ListElementFrequency(Data1,Size,SNum)

    print("Minimum  element in list is : ",Ret)
if __name__ == "__main__":
    main()
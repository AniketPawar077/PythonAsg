from functools import reduce

def FilterNos(List,length):
    fData = []
    iCnt = 0

    for i in range(length):
        iCnt = 0
        for j in range(1,List[i]+1,1):

            if List[i] % j == 0:
                iCnt = iCnt + 1

        if iCnt == 2:
            fData.append(List[i])

    return fData



MapNos = lambda Num : Num * 2

ReduceNos = lambda Num1,Num2 : Num1 if Num2<Num1 else Num2
def main():
    print("Enter the size of List : ")
    Size = int(input())

    Data = []
    
    for i in range(1,Size+1,1):
        print("Enter the list elements : ")
        i = int(input())
        Data.append(i)

    FData = FilterNos(Data,Size)

    MData = list(map(MapNos,FData))

    RData = reduce(ReduceNos,MData)

    print("Filtered Data :- ")
    print(FData)
    

    print("Mapped Data :-  ")
    print(MData)
    print()
    
    print("Reduced Data :-  ")
    print(RData)
    print()

    
    
if __name__ == "__main__":
    main()
from functools import reduce

FilterNos = lambda Num : Num if Num >= 70 else None
MapNos = lambda Num : Num + 10
ReduceNos = lambda Num1,Num2 : Num2 * Num1
def main():
    print("Enter the size of List : ")
    Size = int(input())

    Data = []
    
    for i in range(1,Size+1,1):
        print("Enter the list elements : ")
        i = int(input())
        Data.append(i)

    FData = list(filter(FilterNos,Data))

    MData = list(map(MapNos,FData))

    RData = reduce(ReduceNos,MData)

    print("Filtered Data :- ")
    print(FData)
    print()

    print("Mapped Data :-  ")
    print(MData)
    print()

    print("Reduced Data :-  ")
    print(RData)
    print()
    
if __name__ == "__main__":
    main()
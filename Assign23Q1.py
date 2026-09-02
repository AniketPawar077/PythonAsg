from multiprocessing import Pool
import os
def SumEven(Num):
    print("Process id : ",os.getpid())
    Sum = 0
    for i in range(1,Num+1):
        if ( i % 2 == 0 ):
            Sum = Sum + i
    return Sum
def main():
    Data = []

    print("Enter the size of the List : ")
    Size = int(input())

    for i in range(Size):
        print("Enter the list elements : ")
        i = int(input())
        Data.append(i)

    with Pool(processes=3) as pool:
        Ret = pool.map(SumEven,Data)   

    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()
import os
from multiprocessing import Pool
def Factorials(Num):
    print("Process id : ",os.getpid())
    iFact = 0
    for i in range(1,Num):      
        if Num % i == 0:
            iFact = iFact + i

    return iFact
def main():
    Data = []
    print("Enter the size of list  : ")
    Size = int(input())

    for i in range(Size):
        print("Enter the array elements : ")
        i = int(input())
        Data.append(i)

    with Pool(processes=3) as pool:
        Ret = pool.map( Factorials,Data)

    print("Factorials : ",Ret)
if __name__ == "__main__":
    main()












    
from multiprocessing import Pool
import os
def CountOdd(Num):
    print("Process id : ",os.getpid())
    count = 0
    for i in range(1,Num+1):
        if ( i % 2 != 0 ):
            count = count + 1
    return count
def main():
    Data = []

    print("Enter the size of the List : ")
    Size = int(input())

    for i in range(Size):
        print("Enter the list elements : ")
        i = int(input())
        Data.append(i)

    with Pool(processes=3) as pool:
        Ret = pool.map(CountOdd,Data)   

    print("count of Odd nos present in list elements is : ",Ret)

if __name__ == "__main__":
    main()
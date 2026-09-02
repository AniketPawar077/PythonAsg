from multiprocessing import Pool
import os
def Factorial(Num):
    
    Factorials = 1
    for i in range(Num,1,-1):
        
            Factorials = i * Factorials
    return Factorials
def main():
    Data = []

    print("Enter the size of the List : ")
    Size = int(input())

    for i in range(Size):
        print("Enter the list elements : ")
        i = int(input())
        Data.append(i)

    with Pool(processes=3) as pool:
        Ret = pool.map(Factorial,Data)   

    print("Factorials of nos : ",Ret)

if __name__ == "__main__":
    main()
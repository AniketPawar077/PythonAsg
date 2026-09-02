from multiprocessing import  Pool
import math
def Power5(Num):
    Multi = 0

    for i in range(1,Num+1,1):
        Multi = ((i)**5) +Multi

    return Multi


def main():
    Data  = []
    print("Enter the size of the list :  ")
    Size = int(input())

    for i in range(Size):
        print("Enter the List Elements : ")
        i = int(input())
        Data.append(i)


    with Pool(processes=3)as pool:
        Ret = pool.map(Power5,Data) 

    print("Result is : ",Ret)
if __name__ == "__main__":
    main()
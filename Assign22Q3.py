from multiprocessing import Pool
def CountPrime(Num):
    Count1 = 0 
    Count2 = 0
    for i in range(1,Num+1,1):
        Count1 = 0 
        for j in range(1,i+1,1):
            if i % j == 0:

                Count1 = Count1 + 1
            

        if Count1 == 2:
            Count2 = Count2 + 1
                    
    return Count2
        
    
def main():
    Data = []
    print("Enter the List size : ")
    Size = int(input())

    for i in range(Size):
        print("Enter the list elements : ")
        i = int(input())
        Data.append(i)

    with Pool(processes=3) as pool :
        Ret = pool.map(CountPrime,Data)

    print("Total prime number present in each List elements are like : ",Ret)

if __name__ == "__main__":
    main()


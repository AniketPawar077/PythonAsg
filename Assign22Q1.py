from multiprocessing import Pool

def SquareOfListElements(Num):
    Sum = 0
    for i in range(Num+1):
        Sum =  Sum +(i**2)
        
    return Sum
def main():
    Data = []
    print("Enter the list size : ")
    Size = int(input())

    for i in range(Size):
        print("Enter the list elements : ")
        i = int(input())
        Data.append(i)

    with Pool(processes=3) as pool : 
        Ret = pool.map(SquareOfListElements,Data)

    print("Sum of Square of list elements : ",Ret)


if __name__ == "__main__":
    main()
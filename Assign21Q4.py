import threading
def Sum(List,Leng):
    Sum = 0
    for i in range(Leng):
        Sum = List[i]+Sum
    print("Summation of elements : ",Sum)
def Pro(List,Leng):
    Prod = 1
    for i in range(Leng):
        Prod = List[i]*Prod

    print("Multiplication of elements : ",Prod)

def main():
    Data = []
    print("Enter the size of list : ")
    Size = int(input())

    for i in range(Size):
        print("Enter the list elements : ")
        i = int(input())
        Data.append(i)

    t1 = threading.Thread(target=Sum,args=(Data,Size))
    t2 = threading.Thread(target=Pro,args=(Data,Size))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":

    main()
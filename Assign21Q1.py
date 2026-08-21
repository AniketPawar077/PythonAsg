import threading
def Prime(Leng,List):
    
    print("Prime number : ")
    for i in range(Leng):
        Count = 0
        for j in range(1,List[i]+1,1):
            if List[i] % j == 0:
                Count = Count+1
            
        if Count == 2 :
            print(List[i])
        



def NonPrime(Leng,List):
    Count = 0
    print("Non prime number  : ")
    for i in range(Leng):
        Count = 0
        for j in range(1,List[i]+1,1):
            if List[i] % j == 0:
                Count = Count+1
        if Count > 2 :
            print(List[i])


def main():
    Data = []
    print("Enter the size of list : ")
    Size = int(input())

    for i in range(1,Size+1,1):
        print("Enter the list elements : ")
        i = int(input())
        Data.append(i)

    t1 = threading.Thread(target=Prime,args=(Size,Data))
    t2 = threading.Thread(target=NonPrime,args=(Size,Data))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
if __name__ == "__main__":
    main()
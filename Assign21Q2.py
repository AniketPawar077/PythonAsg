import threading
def MaxElement(Leng,List):
    Max = 0
    print("Max number : ")
    for i in range(Leng):
        if List[i] >Max:
            Max = List[i]

    print(Max) 
        



def MinElement(Leng,List):
    Min = List[0]
    print("Minimum number : ")
    for i in range(Leng):
        if List[i] < Min:
            Min = List[i]

    print(Min) 



def main():
    Data = []
    print("Enter the size of list : ")
    Size = int(input())

    for i in range(1,Size+1,1):
        print("Enter the list elements : ")
        i = int(input())
        Data.append(i)

    Ret = t1 = threading.Thread(target=MaxElement,args=(Size,Data))
    t2 = threading.Thread(target=MinElement,args=(Size,Data))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(" ",Ret)
if __name__ == "__main__":
    main()
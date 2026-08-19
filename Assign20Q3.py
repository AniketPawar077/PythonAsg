import threading

def EvenList(List,Length):
    Sum = 0

    for i in range(Length):
        if List[i] % 2 == 0:
            Sum = Sum +List[i]

    print("Evenlist Summation is : ", Sum)
def OddList(List,Length):
    Sum = 0

    for i in range(Length):
        if List[i] % 2 == 1:
            Sum = Sum +List[i]

    print("list Summation is : ", Sum)


def main():
    Data = []

    print("Enter the size of the list : ")
    Size = int(input())

    for i in range(1,Size+1,1):
        print("Enter the List elements : ")
        i = int(input())
        Data.append(i)


    t1 = threading.Thread(target=EvenList,args=(Data,Size))
    t2 = threading.Thread(target=OddList,args=(Data,Size))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()
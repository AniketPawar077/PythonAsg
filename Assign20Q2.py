import threading
def EvenFactor(Val):
    Sum = 0
    for i in range(1,Val,1):
        if Val % i == 0 and i %2 == 0:
            Sum = Sum + i

    print("Summation of even factors are  : ",Sum)

def OddFactor(Val):
    Sum = 0
    for i in range(1,Val,1):
        if Val % i == 0 and i %2 != 0:
            Sum = Sum + i

    print("Summation of odd factors are  : ",Sum)

def main():
    print("Enter the number  : ")
    Num = int(input())

    t1 = threading.Thread(target=EvenFactor,args=(Num,))
    t2 = threading.Thread(target=OddFactor ,args=(Num,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main thread")
if __name__ == "__main__":
    main()
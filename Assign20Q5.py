import threading
def Thread1(Limit):
    print("Normal order : ")
    for i in range(Limit+1):
        print( " ",i ,end="")

def Thread2(Limit):
    print()
    print("Reverse order : ")
    for i in range(Limit,0,-1):
        print(" ",i ,end="")

def main():
    Length = 50

    t1 = threading.Thread(target=Thread1,args=(Length,))
    t2 = threading.Thread(target=Thread2,args=(Length,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()
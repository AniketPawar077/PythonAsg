import threading
Counter = 0
Lock = threading.Lock()
Counter = 0
def Thread1(Num):
    global Counter 
    for i in range(Num):
   
        Lock.acquire()
        Counter = Counter+1
        Lock.release()

    print("Thread1 Counter:", Counter)
    
def Thread2(Num):
    global Counter
    for i in range(Num):
        Lock.acquire()
        Counter = Counter+1
        Lock.release()
    print("Thread2 Counter:", Counter)
    
def Thread3(Num):
    global Counter
    for i in range(Num):
        Lock.acquire()
        Counter = Counter+1
        Lock.release()
    print("Thread3 Counter:", Counter)


def main():
    t1 = threading.Thread(target=Thread1,args=(5,))
    t2 = threading.Thread(target=Thread2,args=(5,))
    t3 = threading.Thread(target=Thread3,args=(5,))

    
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Total counter : ",Counter)
if __name__ == "__main__":
    main()
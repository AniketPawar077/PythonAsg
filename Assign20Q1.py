import threading
def DisplayEven(Size):
    print("First 10 even numbers : ")
    for i in range(1,Size+1,1):
       if i % 2 == 0:

            print(i)
    
def DisplayOdd(Size):
    print("First 10 Odd numbers : ")

    for i in range(1,Size+1,1):
       if i % 2 == 1:

            print(i)
    
def main():

    t1 = threading.Thread(target=DisplayEven,args=(20,))  
    t2 = threading.Thread(target=DisplayOdd,args=(20,)) 

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
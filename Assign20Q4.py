import threading
def Small(Strings):
    Count = 0
    print("Threading ID : ",threading.get_ident())
    print("Thread Name : ",threading.current_thread().name)
    for i in range(len(Strings)):
        if Strings[i] >= 'a' and Strings[i]<= 'z':
               Count = Count + 1


    print("Number of lowercase",Count)
def Capital(Strings):
    print("Threading ID : ",threading.get_ident())
    print("Thread Name : ",threading.current_thread().name)

    Count = 0

    for i in range(len(Strings)):
        if Strings[i] >= 'A' and Strings[i]<= 'Z':
               Count = Count + 1


    print("Number of Uppercase",Count)
def Numeric(Strings):
    print("Threading ID : ",threading.get_ident())
    print("Thread Name : ",threading.current_thread().name)

    Count = 0

    for i in range(len(Strings)):
        if Strings[i].isnumeric():
            Count = Count + 1


    print("Number of Numbers : ",Count)
def main():
    String = str 

    print("Enter the String  Size : ")
    String =input()


    t1 = threading.Thread(target=Small,args=(String,))
    t2 = threading.Thread(target=Capital,args=(String,))
    t3 = threading.Thread(target=Numeric,args=(String,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    
if __name__ == "__main__":
    main()
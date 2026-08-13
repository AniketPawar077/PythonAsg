def ListElementSum(List1,Length):
    Sum = 0
    for i in range(Length):
     Sum = Sum + List1[i]

    return Sum
            
            
def main():
    Data1 = []
    print("Enter the List Size : ")
    Size = int(input())

    for i in range(1,Size+1,1):
        print("Enter the list elements : ")
        Values = int(input())
        Data1.append(Values)

    Ret = ListElementSum(Data1,Size)

    print("Addition of elements in list is : ",Ret)
if __name__ == "__main__":
    main()
def ListMinElement(List1,Length):
    Min = List1[1]
    for i in range(Length):
     if List1[i] < Min:
        Min = List1[i]

    return Min
            
            
def main():
    Data1 = []
    print("Enter the List Size : ")
    Size = int(input())

    for i in range(1,Size+1,1):
        print("Enter the list elements : ")
        Values = int(input())
        Data1.append(Values)

    Ret = ListMinElement(Data1,Size)

    print("Minimum  element in list is : ",Ret)
if __name__ == "__main__":
    main()
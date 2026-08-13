def ListMaxElement(List1,Length):
    Max = 0
    for i in range(Length):
     if List1[i] > Max:
        Max = List1[i]

    return Max
            
            
def main():
    Data1 = []
    print("Enter the List Size : ")
    Size = int(input())

    for i in range(1,Size+1,1):
        print("Enter the list elements : ")
        Values = int(input())
        Data1.append(Values)

    Ret = ListMaxElement(Data1,Size)

    print("Maximum  element in list is : ",Ret)
if __name__ == "__main__":
    main()
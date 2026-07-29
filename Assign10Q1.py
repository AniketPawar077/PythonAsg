def MultiplicationTable(No1):
    
    for i in range(1,11):
        print(No1," * ",i,"=",(No1 * i))



def main():
    print("Enter the number : ")
    Num = int(input())

    MultiplicationTable(Num)
if __name__ == "__main__":
    main()
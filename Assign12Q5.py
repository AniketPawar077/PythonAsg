def DisplayReverseNumbers(No):
    

    for i in range(No,0,-1):
        print(i)
        

def main():
    print("Enter the number : ")
    Num = int(input())
    DisplayReverseNumbers(Num)
if __name__ == "__main__":
    main()
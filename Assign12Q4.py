def DisplayRangeNumbers(No):
    

    for i in range(1,No+1,1):
        print(i)
        

def main():
    print("Enter the number : ")
    Num = int(input())
    DisplayRangeNumbers(Num)
if __name__ == "__main__":
    main()
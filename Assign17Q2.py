def Display(Num):
    for i in range(1,Num+1,1):
        for j in range(1,Num+1,1):
            print("*", end=" ")
        print()
def main():
    print("Enter the number : ")
    Num = int(input())
    Display(Num)
if __name__ == "__main__":
    main()
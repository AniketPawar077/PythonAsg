def DisplayFactors(No):
    Fact = 0

    for i in range(1,No+1):
        if No % i == 0:
            Fact = i

            print(Fact)
def main():
    print("Enter the number : ")
    Num = int(input())
    DisplayFactors(Num)

if __name__  == "__main__":
    main()
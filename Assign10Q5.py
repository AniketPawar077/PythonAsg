
def DisplayOdd(No):
    print("Odd numbers in between ",No,"is - ")    

    for i in range(1,No+1):

        if i % 2 == 1 :
            print(" ",i)

def main():
    print("Enter the number : ")
    Num = int(input())

    DisplayOdd(Num)
    
if __name__ == "__main__":
    main()
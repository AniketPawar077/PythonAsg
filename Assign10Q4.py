
def DisplayEven(No):
    print("Even numbers in between ",No,"is - ")    

    for i in range(1,No+1):

        if i % 2 == 0 :
            print(" ",i)

def main():
    print("Enter the number : ")
    Num = int(input())

    DisplayEven(Num)
    
if __name__ == "__main__":
    main()
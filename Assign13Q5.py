def DisplayResult(Marks):

    if Marks >= 75:
        print("Distinction")
    elif Marks >= 60:
        print("First Class")
    elif Marks >= 50:
        print("Second Class")
    elif Marks < 50:
        print("Fail") 
def main():
    print("Enter the number : ")
    Num = int(input())

    DisplayResult(Num)

if __name__ == "__main__":
    main()
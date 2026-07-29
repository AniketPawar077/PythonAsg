#binary equivalent program
def Binary(No):
    print(f"The binary equivalent of {No} is {bin(No)}") # in this function we are using bin() function to convert decimal to binary equivalent

def main():
    print("Enter the number : ")
    Num = int(input())
    Binary(Num)

if __name__ == "__main__":
    main()
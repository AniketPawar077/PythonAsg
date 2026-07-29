CheckDivisibility = lambda Value : Value % 5 == 0
 
def main():
    print("Enter the number : ")
    Num = int(input())

    ret = CheckDivisibility(Num)

    if ret == True:
        print(True)
    
if __name__ == "__main__":
    main()
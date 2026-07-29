Addition = lambda Val1,Val2 : Val1 + Val2 
 
def main():
    print("Enter the number : ")
    Num1 = int(input())
    print("Enter the number : ")
    Num2 = int(input())

    ret = Addition(Num1,Num2)

    print("Addition of both numbers : ",ret)
    
if __name__ == "__main__":
    main()
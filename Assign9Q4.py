def CalculateCube(No1):
    Cube = No1 * No1 *No1

    return Cube
    
def main():
    print("Enter the  number : ")
    Num1 = int(input())

    Ret = CalculateCube(Num1)

    print(Num1," Cube is : ",Ret)
         
if __name__ == "__main__":
    main()
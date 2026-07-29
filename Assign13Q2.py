def AreaCircle(radius,pi):
    AreaCirc = pi*radius*radius
    return AreaCirc

def main():
    print("Enter the Radius of Circle : ")
    Radi = float(input())
    
    
    Pi = 3.14
    Ret = AreaCircle(Radi,Pi)

    print("Area of Circle is : ",Ret)

if __name__ == "__main__":
    main()
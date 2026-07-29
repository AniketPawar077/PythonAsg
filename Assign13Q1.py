def AreaRectangle(length,width):
    AreaRec = length * width
    return AreaRec

def main():
    print("Enter the lentgh of Rectangle : ")
    Leng = float(input())
    
    print("Enter the Width of Rectangle : ")
    Wid = float(input())

    Ret = AreaRectangle(Leng,Wid)

    print("Area of rectangle is : ",Ret)

if __name__ == "__main__":
    main()
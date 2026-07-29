
def SummationNaturalNumbers(No1):
    Sum = 0
    Sub = 0

    for i in range(1,No1+1):
        Sum = Sum + i
        
    return Sum

def main():
    print("Enter the number : ")
    Num = int(input())

    ret = SummationNaturalNumbers(Num)
    print("Summation of first natural numbers : ",ret)
    
if __name__ == "__main__":
    main()
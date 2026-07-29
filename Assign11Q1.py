
def CheckPrime(No):
    Fact = 0
    Count = 0
    

    for i in range(1,No+1):
        
        if No % i == 0:
            
            Fact = Fact+1
        
    if Fact == 2:
        print("It is a prime number")
           
    elif Fact == 1 :
           print("it is not a prime")
    else :
           print("it is not a prime number ")
            
            
        
def main():

    print("Enter the number  : ")
    Num = int(input())

    CheckPrime(Num)

   
if __name__ == "__main__":
 main()
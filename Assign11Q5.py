def Palindrome(No):
    Original = No
    Reverse = 0
    digit = 0
    while No != 0 :
        
        digit = No % 10 
        Reverse = Reverse * 10 + digit  
        '''
        Reverse = Reverse * 10 + digit means that we are multiplying the current value of Reverse by 10 and then adding the new digit to it.
        This effectively shifts the digits of Reverse to the left and adds the new digit at the end, building the reversed number 
        step by step.
        '''
        No = No // 10       

    if Original == Reverse:
        return True
    else :
        return False


def main():

    print("Enter the number : ")
    Num = int(input())

    Ret = Palindrome(Num)

    if Ret == True:
        print("Yes, the number is a palindrome")    
    else:
        print("No, the number is not a palindrome")

if __name__ == "__main__":
    main()
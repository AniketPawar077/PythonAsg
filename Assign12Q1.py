def CheckVowels(char):

    if char == 'a' or char == 'e' or char =='i' or char =='o' or char=='u' or char == 'A' or char == 'E' or char =='I' or char =='O' or char=='U' :
        return True
    else :
        return False
     
        
def main():
    print("Enter the character : ")
    Char = str(input())

    Ret = CheckVowels(Char)

    if Ret == True :
        print(Char," It is a vowel")
    else :
        print(Char," It is a consonant")

if __name__ == "__main__":
    main()
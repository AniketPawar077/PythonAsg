import sys 

print("Enter the number : ")
Intnum = int(input())
print("Enter the charcters  : ")
Cchar = input()

print(type(Intnum))
print(id(Intnum))
print(sys.getsizeof(Intnum))

print(type(Cchar))
print(id(Cchar))
print(sys.getsizeof(Cchar))
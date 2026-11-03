
class Arithmatic :

 def  __init__(self,val1,val2):
    self.val1 = val1
    self.val2 = val2
 def __init__(self):
   self.val2 = 0
   self.val1 = 0

 def Accept(self):
   self.val1 = int(input("enter the first number : "))
   self.val2 = int(input("enter the second number : "))
   
 def Addition(self):
   print("Addition of both number : ",self.val1+self.val2)
 def Substraction(self):
   print("Substraction of both number : ",(self.val1-self.val2))
 def Multiplication(self):
   print("Multiplication of both number : ",self.val1*self.val2)
 def Division(self):
   if self.val1 == 0 or self.val2 == 0:
      print("Invalid operation beccause of zero division")
   else :
     print("Division is : ",self.val1 / self.val2)

     print("--------------------------------------------------------------------------------------------")

obj1 = Arithmatic()
obj1.Accept()
obj1.Addition()
obj1.Substraction()
obj1.Multiplication()
obj1.Division()

obj2 = Arithmatic()
obj2.Accept()
obj2.Addition()
obj2.Substraction()
obj2.Multiplication()
obj2.Division()

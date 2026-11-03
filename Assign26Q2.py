class Circle:
    pi  = 3.14

    def __init__(self,radius,Area,Cicumference):
        self.radius = radius
        self.Area = Area
        self.Cicumference = Cicumference

    def __init__(self):

        self.radius = 0.0
        self.Area = 0.0
        self.Cicumference = 0.0

    def Accept(self):
            self.radius = float(input("Enter the radius of circle : "))

    def CalculateArea(self):
            self.Area = self.pi * self.radius * self.radius 

    def CalculateCircumference(self):
            self.Circumference = 2 * self.pi * self.radius

    def Display(self):
            print("Radius of Circle is : ",self.radius)
            print("Area of Circle is : ",self.Area)
            print("Circumference of Circle is : ",self.Circumference)


obj1 = Circle()
obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()  

obj2 = Circle()
obj2.Accept()
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()







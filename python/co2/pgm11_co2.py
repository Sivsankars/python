x = int(input("Enter the length of square: "))
area1 = lambda x:(x*x)
print("Area of square is: ",area1(x))

y = int(input("Enter the length of rectangle: "))
z = int(input("Enter the breadth of rectangle: "))
area2 = lambda y,z:(y*z)
print("Area of rectangle is: ",area2(y,z))

area3 = lambda a,b:(.5*(a*b))
a = int(input("Enter the length of base: "))
b = int(input("Enter the height: "))
print("Area of triangle is: ",area3(a,b))

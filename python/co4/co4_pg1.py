class Rectangle:
    def __init__(s,val1,val2):
        s.length=int(val1)
        s.breadth=int(val2)
    def area(s):
        return s.length*s.breadth
    def perim(s):
        return 2*(s.length+s.breadth)
r1=Rectangle(input("Enter length of 1st rectangle"),input("Enter breadth of 1st rectangle"))
r2=Rectangle(input("Enter length of 2nd rectangle"),input("Enter breadth of 2nd rectangle"))       

if(r1.area()>r2.area()):
    print("area of 1st is larger")
else:
    print("area of 2nd rectangle is larger")

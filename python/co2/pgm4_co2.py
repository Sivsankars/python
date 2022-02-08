import math
lim1 = int(input("Enter starting limit: "))
lim2 = int(input("Enter ending limit: "))
list1=[]
list2=[]

for x in range(lim1, lim2):
    if x % 2 == 0:
        a=x//10
        b=a//10
        c=b//10
        d=c//10
        if(a%2==0 and b%2==0 and c%2==0 and d%2==0):
            list1.append(x)
for y in list1:
    if y>999 and y<10000:
        if (math.ceil(math.sqrt(y)) ==  math.floor(math.sqrt(y))):
            list2.append(y)
print(list2)

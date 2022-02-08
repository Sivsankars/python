list1=[]
list2=[]
for x in range(0,5):
    a=input("Enter a word: ")
    list1.append(len(a))
    list2.append(a)
print(list2)
print("Length of longest word is ",max(list1))

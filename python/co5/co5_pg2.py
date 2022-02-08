fn=open("hello.txt","r")
fr=open("yes.txt","w")
count=fn.readlines()
for i in range(0,len(count)):
    if(i%2!=0):
        fr.write(count[i])
    else:
        pass
fn.close()
fr.close()
f=open("yes.txt","r")
r=f.read()
print(r)
f.close()
    
    

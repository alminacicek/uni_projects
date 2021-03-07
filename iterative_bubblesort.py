def bubble(l):
    moved=1
    while moved==1:
        moved=0
        for i in range (0,len(l)-1):
            if(l[i+1]<l[i]):
                l[i],l[i+1]=l[i+1],l[i]
                moved=1
    return l


l=[]

a=int(input("How many numbers are there in our list?"))

for i in range(0, a): 
    element = int(input()) 
  
    l.append(element)

print(bubble(l))


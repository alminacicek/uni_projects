def factorial(n):
    a=1
    for i in range (1,n+1):
        a*=i
    return a

b=int(input("Enter a:"))
c=int(input("Enter b:"))

def combination(b,c):
    result= factorial(b)//(factorial(c)*factorial(b-c))
    return result
    
print("The combination of the numbers",b,"and",c,"are",combination(b,c))

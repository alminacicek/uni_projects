def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
        
n =int(input("Which member of the fibonacci serie do you want to find?"))

print("The",n,"number of fibonacci is",fibonacci(n))
        


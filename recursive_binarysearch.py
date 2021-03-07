def binary_search (l,left,right,key):
    if (right>left):
        mid=int((left+right)//2)
        if (l[mid]==key):
            return mid
        elif(key<l[mid]):
            return binary_search(l,left,mid-1,key)
        else:
            return binary_search(l,mid+1,right,key)
    else:
        return -1
        
l=[1,2,3,4,5,6,7,8,9,10]

n = int(input("Which value do you want to know the place of ?"))

result = int(binary_search(l, 0, len(l)-1, n))

print("Value is present at index "+ str(result))

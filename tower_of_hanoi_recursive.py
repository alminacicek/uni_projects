def move (n,start,temp,final):
    #n is the number of discs we move from start to temp to
	if n==1:
		print("Moved disc", n , "from", start, "to",final)
		#here we remove the n'th disc
	else:
		move(n-1,start,final,temp)
		#we move n-1 discs  to temp
		print("Moved disc",n,"from",start,"to",final)
		move(n-1,temp,start,final)
		#we move n-1 discs  to final

n=int(input("How many discs are there to be moved?"))
print(move(n, "A", "B", "C"))



A = [3,45,7,4,7,865,84,4,53,76,658]

#recursive de bir durma koşulu lazım (burada list tek bir elemansa)
#ayrıca son elemanın başka bir yerde tekrar etmemesi lazım yoksa orada listi saymayı bitirir

#1.yöntem
def length():
    if A[0] == A[-1]:
        return 1
    return length(A[1:])+1
    
#2.yöntem
def length(A, index):
    if A[index] == A[-1]:
        return index+1
    return length(A, index+1)


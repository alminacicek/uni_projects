def printMatrix(row_count,column_count,list_matrix,name_matrix):
    nameOfMatrix = name_matrix
    print(nameOfMatrix)
    print('\n')
    for i in range(0,row_count):
        for j in range(0, column_count):
            print(list_matrix[i*column_count + j], end = ' ')
        print('\n')
        
print(printMatrix(1,2,2,"apply"))


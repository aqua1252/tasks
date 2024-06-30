def op(matrix):
    z=[]
    def zeros(a,b):
        z.append(a)
        z.append(b)
    def findzeros(matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    zeros(i,j)
                    
    def setzero(i,j):
        for k in range(len(matrix)):
            for h in range(len(matrix[0])):
                matrix[k][j]=0
                matrix[i][h]=0
                      
    findzeros(matrix)       

    for k in range(0,len(z),2) :
             i=z[k]
             j=z[k+1]
             setzero(i,j)
    print(matrix)
matrix1 = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 2]] 
matrix2 = [
    [0, 2, 3],
    [4, 0, 6],
    [7, 8, 2]] 
op(matrix1)
op(matrix2)

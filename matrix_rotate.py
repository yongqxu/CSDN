matrix =[]
n = input('size: ')
n = int(n)

def printMatrix(mt):
    for arow in mt:
        print(arow)

def rotate(mt):
    for i in range(n):
        for j in range(i, n):
            tmp = mt[i][j]
            mt[i][j] = mt[j][i]
            mt[j][i] = tmp

for i in range(0, n):
    arow = []
    for j in range(1, n+1):
        arow.append(n*i+j)
    matrix.append(arow)
printMatrix(matrix)
rotate(matrix)
print('After rotate')
printMatrix(matrix)




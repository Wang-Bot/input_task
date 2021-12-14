#Matrix A [[1, 2, 3, 4]]
#Matrix B [[5, 6, 7, 8]]
#output:  [[6, 8, 10, 12]]

m = int(input("Enter the value of m"))
n = int(input("Enter the value of n"))

def matrix(m,n):
    o = []
    for i in range(m):
        row = []
        for j in range(n):
            inp=int(input(f'Enter the o[{i}][{j}]'))
            row.append(inp)
        o.append(row)
    return o


def sum(A,B):
    output=[]
    for i in range(len(A)): #number of rows
        row = []
        for j in range(len(A[0])):  #number of columns
            row.append(A[i][j]+B[i][j])
        output.append(row)
    return output
A=matrix(m,n)
print("Matrix A",A)

B=matrix(m,n)
print("Matrix B",B)

s=sum(A,B)
print("Summation of given two matrices are:")
print(s)























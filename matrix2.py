R = int(input("Number of Rows: "))
C = int(input("Number of Columns: "))

matrix = []
print("Insert entries row-wise: ")

for i in range(R):
    a = []
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)
    
    
for i in range(R):
    for j in range():
        print(matrix[i][j], end = "")
    print()
    

for i in range(R):
    C = list(map(int, input().split))
    matrix.append(C)
print(matrix)
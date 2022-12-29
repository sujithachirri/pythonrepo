m=int(input())
n=int(input())
mat=[]
for i in range(m):
    row=input().split()
    for j in row:
        mat.append(j)
mat.sort()
k=0
for i in range(m):
    for j in range(n):
        print(mat[k],end=' ')
        k=k+1
    print()
#第一问
import numpy as np
import random
rows=5
cols=10
M1=np.random.randint(1,51,size=(rows,cols))
print(M1)
rows1=10
cols1=5
M2=np.random.randint(1,51,size=(rows1,cols1))
print(M2)

#运用numpy库来执行矩阵乘法
#c=np.dot(M1,M2)

#第二问
#用for语句来执行
def Matrix_multip():
    n1 = int(input('请输入方阵的行或列'))
    M3 = []
    for i in range(n1):
        M3.append(list(map(int, input('输入每行').rstrip().split())))
    n1 = int(input('请输入方阵的行或列'))
    M4 = []
    for i in range(n1):
        M4.append(list(map(int, input('输入每行').rstrip().split())))#rstrip去除右侧空格指定字符串,split（）遇到空格了分割
# 获取矩阵A的行数和列数
    rows_A = len(M3)
    cols_A = len(M3[0])

# 获取矩阵B的行数和列数
    rows_B = len(M4)
    cols_B = len(M4[0])
#创建初始矩阵，两种方式
#M3a=[[0 for _ in range(cols_A)] for _ in range(rows_A)]
#M3b=[[0 for _ in range(cols_A)] for _ in range(rows_A)]
    M3a=np.zeros((rows_A,cols_B))
    M3b=np.zeros((rows_B,cols_B))
    for i in range(rows_A): # 矩阵的行
        for j in range(cols_B):   # 矩阵的列
            M3b[i][j] = M3b[i][j] + M3[i][j] + M4[i][j]
            for k in range(rows_A):
               M3a[i][j]=M3a[i][j]+M3[i][k]*M4[k][i]

    print('两矩阵相乘得出：',M3a)
    print('两矩阵相加得出：',M3b)
Matrix_multip()


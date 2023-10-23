K= int(input('请输入显示第几行'))
a = []
for i in range(1, K+1):
    a.append(list(1 for j in range(1, i + 1)))
    if i > 2:
        for n in range(1, i - 1):
            a[i - 1][n] = a[i - 2][n - 1] + a[i - 2][n]
for k in range(0, i):
    print(a[i - 1][k], end=' ')
print("")
def Least_moves(n):
    # 创建一个列表dp，用于存储从1到n的每个数字所需的最小步数
    a=[0]*(n + 1)
    # 从2开始遍历到n
    for i in range(2, n + 1):
        # 初始化当前数字i所需的步数为前一步的步数加1
        a[i] = a[i - 1] + 1
        # 如果当前数字是偶数，尝试用除2的操作来减小步数,和前一步的步数比较求最小
        if i % 2 == 0:
            a[i] = min(a[i],a[i//2]+1)
    # 返回n所需的最小步数
    return a
# 输入n
n=int(input("请输入一个整数 n: "))
b=Least_moves(n)
print("从1到"+str(n)+"所需的最小步数是:"+str(b[n]))

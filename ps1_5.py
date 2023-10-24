import random
from itertools import product

import matplotlib.pyplot as plt

digits = "123456789"

def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except:
        return None
valid_expressions = []
C=[]#定义空list
D=[]#定义空list
Total_solutions=[]#定义空list
for target in range(0,101):
# 生成所有可能的运算符排列组合
   for p in product("+- ", repeat=len(digits) - 1):  #将所有运算符排列的可能性赋给p

       expression=''.join(d+op for d, op in zip(digits, p)) + digits[-1]
    #zip(digits, p)，将每个数字与p中每个运算符配对，再将配对后的序列生成一个字符串输出
    # 移除空格
       expression = expression.replace(" ", "")
       result = evaluate_expression(expression)
       if result is not None and result == target:
           valid_expressions.append(expression)
   #print(valid_expressions)  # 输出所有得出target的可能性
   b=int(target)#定义索引
   C.append(b)
   Total_solutions=int(len(valid_expressions))
   D.append(Total_solutions)
   valid_expressions=[]#将结果list赋为空，进行第二次循环
print(C)#创建画图时候所需要的x的内容
print(D)#创建画图时候所需要的y的内容
plt.plot(C,D)
plt.show()
   #print(str(target)+':'+str(len(valid_expressions)))






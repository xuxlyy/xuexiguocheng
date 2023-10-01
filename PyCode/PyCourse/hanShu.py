import math
result = math.sin(1)
print(result)
#注释单行
#快捷键仍为ctrl+/
"""
进行
多行
注释
"""

#数据类型-字符串
len("hi\"")
print("hi"[1])

#布尔
b1=True
b2=False

#空值
n=None

#函数实现BMI计算器
def BMI_calculator(height,weight):
    BMI = weight/(height**2)
    if BMI<=18.5:
        cat="偏瘦"
    elif BMI<=25:
        cat="正常"
    elif BMI<=30:
        cat = "偏胖"
    else:
        cat="肥胖"
    print(f"您的BMI分类为{cat}")
    return BMI

BMI_calculator(1.8,70)


#内置函数与引入模块
import math
result = math.sin(1)
print(result)

from statistics import median,mean
print(median([19,-5,36]))

from statistics import *
print(median([19,-5,36]))
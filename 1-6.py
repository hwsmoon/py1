import math
n = int(input("반지름 r 입력 : "))
s=4*math.pi*(n**2)
v=(4/3)*math.pi*(n**3)
print("겉면적 : %f, 부피 : %f" %(s,v))
import random
c=1
c1=0

while True:
    a=random.randint(1,9)
    b=random.randint(1,9)

    q=print("%dX%d"%(a,b))
    u=int(input("정답:"))
    if (u == (a*b)):
        c1+=1

    d = input("문제를 계속 푸시겠습니까?")
    if d=="y":
        c+=c
        continue
    elif d=="n":
        print("정답률:%d" %(c1/c*100))
        break










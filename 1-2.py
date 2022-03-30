sum=0
n = int(input("자연수 N 입력 : "))
for i in range(0,n,2):
    sum+=i
print("결과 : %d" % sum)
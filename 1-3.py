def factorial(n):
    sum = 1
    for i in range(1, n+1, 1):
        sum *= i
    print("결과 : %d" % sum)
n = int(input("자연수 N 입력 : "))
factorial(n)
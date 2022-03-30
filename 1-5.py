a = int(input("Enter a temperature: "))
b = input("Convert to (F)ahrenheit or (C)elsius? ")
if b=="F":
    f=(9/5)*a+32
    print("%d C = %d F" %(a, f))
elif b=="C":
    c=(5/9)*(a-32)
    print("%d F = %d C" %(a, c))

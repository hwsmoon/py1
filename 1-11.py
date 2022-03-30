
t = ["1: Opens a file for reading only in binary.","2: The file pointer is placed.","3: This is the default mode."]
f = open("C:/Users/홍성옥/OneDrive/바탕 화면/file.txt", 'w')
try:

    for i in range(0, 3):
        data = t[i]
        f.write(data)
        f.write("\n")
except FileNotFoundError:

    f.close()
f = open("demofile.txt","a")
f.write("hello welcome to python, python is a very simple and reliable language,without any pogramming knowledge,we can learn easily")
f.close()
file  =  open("demofile.txt", "r")
data  = file.read()
li  =  data.split(",")
for line in li:
    print(line)
file.close()



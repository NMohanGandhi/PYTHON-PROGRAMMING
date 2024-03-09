#def registration:
file =  open("Demo.txt","a")
user_input1 = input("enter your valid email id")
user_input2 = input("enter your password")

di={}
di[user_input1] = user_input2
file.write(str(di))
file.write('\n')
print(di)
file.close()



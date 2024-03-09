file = open("mohan.txt","a")
print(" please register your valid e_mail id and password")
user1=input("enter your e-mail id")
user2=input("enter your password")
di={}
di[user1] = user2
file.write(str(di))
file.write('\n')
print(di)
file.close()
file = open("mohan.txt","a")
print("please check your e_mail id and password VALID or NOT")
user3=input("enter you e_mail id")
user4=input("enter your password")
dii = {}
di[user3] = user4
file.write(str(dii))
file.write('\n')
print(dii)
if di==dii:

    print("you email and password are valid")
else:
    print("not valid,please register your email and password")
    
            


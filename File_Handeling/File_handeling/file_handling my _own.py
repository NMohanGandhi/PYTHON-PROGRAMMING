file = open("registration.txt","a")
print("choice1 - registration", "choice2 - login" )

choice = int(input("enter your choice number "))
def registration():
    print("please register your email id ,password")
    user1= input("registerwith   your email id")                                                                                                                                                                                                                                                                    
    user2=input("register your password")
    dic1={}
    dic1[user1] = user2
    file.write(str(dic1))
    file.write('\n')
    print(dic1)
    file.close()



def login() :
    print("login your account")
    
    login_user = input(" login  with your email id :  ")
    login_pass =input(" login with your password   ")

    logfile  = open('registration.txt', 'r')
    #print(logfile.read()                                                                                                                                                                                                                                    
    for line in logfile.readlines():

        val  = eval(line)  # dictionary
        #print(val.items())
        
        for keys, values in val.items():
            flag  =  False
            #print(keys)
            #print(values)
            if (login_user  == keys) and (login_pass == values):
                print("Your credentials are correct, welcome to Mohan's world")
                flag = True
                break
            else:
                flag  = False
        if flag == True:
            break

    if flag  == False:
        print("invalid username/password, kindly register if you are a new user")
    file.close

if choice==1:
    registration()
    user_input = input("do you want login into your account(yes/no)")
    if user_input=="yes":
        login()
    else:
        print("thank you for registration,you have sucessfully registerd")
    
else:
    login()
    
    




    


    

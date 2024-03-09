
inp  =  input("welcome to muthyalamma festival trust, enter (yes/no) if there is anyone's donations to enter  :")

inp = "yes"

file  =  open("donations.txt",'a+')

while inp == "yes":
    
    data = {}
    #print(data)
    name  =  input("please enter their name :")
    amt     = input("please enter the donation :")

    data[name] = amt
    print(data)
    file.read( )
    inp  =  input("are you going to add anyone , to add donations (yes/no):")

else:

    print("thank you, now count the donations and check whether anyone has not yet donated ")


    

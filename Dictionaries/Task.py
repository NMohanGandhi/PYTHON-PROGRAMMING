print("WELCOME TO THE UPCOMPING MUTHYALAMMA JATHARA ")
dic = {}
opinion=input("do you want to go another another house(yes/no) : ")
while opinion=="yes":
    house_holder_name = input("enter your name : ")
    houseno= int(input("enter your house identity number : "))
    amount = int(input("enter your amount : "))
    opinion=input("do you want to go another another house(yes/no) : ")

    dic[houseno]=[house_holder_name,amount]
print(dic.values())

  


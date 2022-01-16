import pandas as pd

df= pd.read_csv("User_Profile.csv")
#print(df)
#print("=======================================")

df_columns=df.columns.tolist()

#print(df_columns)
#print("=======================================")
data_dict={}

for index,i in enumerate (df[df_columns[0]].tolist()):
    data_dict.update({i:[df[df_columns[1]][index],df[df_columns[2]][index],df[df_columns[3]][index],df[df_columns[4]][index],df[df_columns[5]][index]]})
#print(data_dict)
#print("=======================================")
    

def signin(action):    
    account_no=5
    while True :
        if start_up_action=="s":
            username = input('Write username :')
            print("=======================================")
            while username!="": 
                if username in data_dict.keys():
                    print("User already exists")
                    print("=======================================")
                    break
                elif username not in data_dict.keys():
                    password= input('Write a password :')
                    while password!='':
                        balance=0
                        transections=0
                        received=0
                        data_dict.update({username:[account_no,balance,transections,received,password]})
# data_dict.to_excel("User_Profile.csv")
                        print("=======================================")                    
                        print('You have successfully sign in',username)
                        print("=======================================")
                        username=''
                        break
        account_no+=1


        break
        


def logged_in_action(username):
    
    for items in data_dict:
        while True:
            if username in data_dict.keys():
                action=input("1-To Check Profile\n2-To Check Balance"\
                              "\n3-To Send Money\n4-To delete your account\n5-To exit\n")
   #Checking Profile
                if action=='1':
                    print("=======================================")
                    print(df_columns[1:5],'\n',data_dict[username][:4])
                    print("=======================================")
   #Checking Balance
                elif action=='2':
                    print("=======================================")
                    print("Your Current Balance is :",data_dict[username][1])
                    print("=======================================")
   #Sending Money
                elif action=='3':
      #Checking if the receiver exists
                    while True:
                        print("=======================================")
                        username2=input("Enter the username of receiver :")
                        if username2 in data_dict.keys():
                            print("")
      #Checking if you have enough balance
                            while True:
                                amount=int(input("Enter the amount you want to send :"))
                                if amount>data_dict[username][1]:
                                    print("=======================================")
                                    print("You don't have enough Money")
                                    print("=======================================")
                                else:
      #updating balance
                                    new_balance=int(data_dict[username][1])-amount
                                    data_dict[username][1]=data_dict[username][1]-amount
      #updating transeection
                                    data_dict[username][2]=int(data_dict[username][2])+amount
      #updating received amount and balance
                                    data_dict[username2][3]=int(data_dict[username2][3])+amount
                                    data_dict[username2][1]=int(data_dict[username2][1])+amount
      #updating dict
                                    data_dict.update
                                    print("=======================================")
                                    print("Money sent successfully")
                                    print("=======================================")
                                    print("User Remaining balance is :",new_balance)
                                    
                                    print("=======================================")
                                    #print(data_dict)
                                    print("=======================================")
                                break
      #Checking if the receiver exists              
                        elif username2 not in data_dict.keys():
                            print("=======================================")
                            print("Sorry User NOt found!!")
                            print("=======================================")
                            break


                        break
            
  #Delete your account           
                
                elif action=='4':
                    print("=======================================")
                    confirming=input("Are you sure you want to delete your account?\n")
                    if confirming =='yes':
                        del data_dict[username]
                        print("Your account deleted successfully")
                        print("=====================================================")
                        data_dict.update
                    
                    else:
                        print("=======================================")
                        print("===Couldn't confirm=== \nReturning to Home Page")
                        print("=====================================================")
                    break
   #Exiting to Login page
                elif action=='5':
                    print("=====================================================")
                    break
        break

                








     
def login(action):
    logged_user=''
    while True :
        if action=='l':
            print("=======================================")
            username=input("Enter your username:")
            for items in data_dict:
                    if username in data_dict.keys():
                        print("User found")
                    else:
                        print("=======================================")
                        print('User NOt found')
                        print("Re-Try")
                        print("=======================================")
                        
                        break
                    print("=======================================")
                    password = input('enter your password :')
                    if password==data_dict[username][4]:
                        print("=======================================")
                        print('welcome ',username)
                        print("=======================================")
                        logged_in_action(username)
                        print("=====================================================")
                        break
                        
                    else:
                        print('wrong password')
                        print("Re-Try")
                        break
            break
        
                    
                        
        else:
            print("Abra ka dabra")
            break
                    
def dataframe_list(index):
    arr=[]
    #print(index,"+")
    for i in data_dict:
        
        arr.append(data_dict[i][index])

    return arr
        

def update_data():
    updated_dict={}
    col=df_columns
    #print(col)
    updated_dict.update({col[0]:data_dict.keys()})
    col.pop(0)
    #print(col)
    for i,key in enumerate(col):
        updated_dict.update({key:dataframe_list(i)})
    dataframe=pd.DataFrame(updated_dict)
    print("=======================================")
    print(dataframe)
    
    dataframe.to_csv("User_Profile.csv",index=False)


def user():
    while True:
        print("=======================================")
        print("=========Welcome to User page==========")
        start_up_action=input("To login enter l\nTo sign-up enter s \
                           \n Press 0 to exit: \n" )
        if start_up_action=="s":
            signin(start_up_action)
        elif start_up_action=='l':
            login(start_up_action)
        elif start_up_action=='0':
            update_data()
            print("=======================================")
            print("Exits window")
            break
        else:
            print("Wrong input")
            print("=====================================================")

def admin():
    admin_username='saad07'
    admin_password='saad23'
    
    print("=======================================")
    print("=========Welcome to Admin page==========")
    ad_username=input("Enter your username :")
    if ad_username==admin_username:
        ad_password=input("Enter your password :")
        if ad_password==admin_password:
            while True:
                print("=======================================")
                print("===========Welcome Mr.Saad=============")
                print("=======================================")
                start_up_action=input("Enter\n1-To check total users data\n2-To edit account info\n3-To return to main manue\n")
                print("=======================================")
                if start_up_action=='1':
                    update_data()
                    print("=======================================")
                elif start_up_action=='2':
                    username=input("Enter the username you want to edit profile :")
                    if username in data_dict.keys():
                        print("=======================================")
                        print(df_columns)
                        print(data_dict[username])
                        print("=======================================")
                    if username in data_dict.keys():
                        print("=======================================")
                        new_balance=input("Enter the new balance :")
                        print("=======================================")
                        new_transaction=input("Enter the new transaction amount :")
                        print("=======================================")
                        new_received=input("Enter the new received amount :")
                        data_dict[username][1]=int(new_received)
                        data_dict[username][2]=int(new_transaction)
                        data_dict[username][3]=int(new_balance)
                        data_dict.update
                        update_data()
                    else:
                        print("=======================================")
                        print("Invalid input")
                elif start_up_action=='3':
                    print()
                    break
    
            else:
                print("=======================================")
                print("Wrong Password Please Try Again")
                print("=======================================")
        else:
            print("=======================================")
            print("User NOt Found Please Try again")
            print("=======================================")
    
                        
    

    
        
while True:
    print("********************************************************************")
    print("*                                                                  *")
    print("*             Welcome to E-Banking  Management System              *")
    print("*                                                                  *")
    print("********************************************************************")
    main_action=input("Enter\n1-To proceed as admin\n2-To proceed as User\n")
    print("=======================================")
    
    if main_action=='1':
        admin()
    elif main_action=='2':
        user()
        break
    else:
        print("Invalid input")

        


        
        
                

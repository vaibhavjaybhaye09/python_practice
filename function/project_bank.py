

import datetime

# depost  Opration
def deposit(balance):
        amount = int(input("\n 💵 Enter the amount to deposit : = "))
        balance = balance + amount
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n ✅ Deposit successful at {current_time}")
        print("\n 💰 Your current balance is: = ", balance)
        print("\n 💵 YOur creadited amount is := ", amount)

# Withdraw Opration
def withdraw(balance):
    amount = int(input("\n 💸 Enter the amount to withdraw you want : = "))
    if amount > balance:
        print("\n ⚠️ !!!!! Insufficient balance !!!!! ⚠️")
    else:
        if amount < 100000:
            balance = balance - amount
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"\n ✅ Withdrawal successful at {current_time}")
            print("\n 💸 Your Debited amount is := ", amount)
            print("\n 💰 Your current balance is : = ", balance)
        else:
            print("\n ⚠️ !!!!! Maximum limit is You withdraw 100000 !!!!! ⚠️")
    return balance

# Check Balance Opration
def check_balance(balance):
      username = (input("\n 👤 Enter Username : "))
      password = (input("\n 🔑 Enter Password : ")) 
      if username != "vaibhavjaybhaye" or password != "999":
        print("\n ⚠️ !!!!! Invalid Username or Password !!!!! ⚠️")
        exit()
      else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n ℹ️ Balance checked at {current_time}")
        print("\n 💰 Your current balance is : = ", balance)

#loan apply opration
def apply_loan():
      username = (input("\n 👤 Enter Username : "))
      password = (input("\n 🔑 Enter Password : ")) 
      if username != "vaibhavjaybhaye" or password != "999":
        print("\n ⚠️ !!!!! Invalid Username or Password !!!!! ⚠️")
        exit()
      else :
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        amount = (input("\n 💵 Enter loan amount: = "))
        print(f"\n ✅ Loan application for {amount} submitted at {current_time}")
        print("\n ℹ️ Our team will contact you soon for further processing.")

# Credit card apply opration
def apply_credit_card():
      username = (input("\n 👤 Enter Username : "))
      password = (input("\n 🔑 Enter Password : ")) 
      if username != "vaibhavjaybhaye" or password != "999":
        print("\n ⚠️ !!!!! Invalid Username or Password !!!!! ⚠️")
        exit()
      else:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n ✅ Credit card application submitted at {current_time}")
        print("\n ℹ️ Our team will contact you soon for further processing.")
  
# Debit card apply opration
def apply_debit_card():
      username = (input("\n 👤 Enter Username : "))
      password = (input("\n 🔑 Enter Password : ")) 
      if username != "vaibhavjaybhaye" or password != "999":
        print("\n ⚠️ !!!!! Invalid Username or Password !!!!! ⚠️")
        exit()
      else :
       current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       print(f"\n ✅ Debit card application submitted at {current_time}")
       print("\n ℹ️ Your debit card will be delivered within 7 days.")

# Passbook apply opration
def apply_passbook():
      username = (input("\n 👤 Enter Username : "))
      password = (input("\n 🔑 Enter Password : ")) 
      if username != "vaibhavjaybhaye" or password != "999":
        print("\n ⚠️ !!!!! Invalid Username or Password !!!!! ⚠️")
        exit()
      else :
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n ✅ Passbook application submitted at {current_time}")
        print("\n ℹ️ Your passbook will be delivered within 7 days.")

# Cheque book apply opration
def apply_cheque_book():
      username = str(input("\n 👤 Enter Username : "))
      password = int(input("\n 🔑 Enter Password : ")) 
      if username != "vaibhavjaybhaye" or password != "999":
        print("\n ⚠️ !!!!! Invalid Username or Password !!!!! ⚠️")
        exit()
      else :
       current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       print(f"\n ✅ Cheque book application submitted at {current_time}")
       print("\n ℹ️ Your cheque book will be delivered within 7 days.")

# Exit opration
def exit():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n 👋 Thank you for using our services. Logged out at {current_time}")
    
    
    


print("\n 💰 ***** Welcome to the Bank Management System ***** 💰")

print("\n Bank Menu Options :")
print("\n 11.   Create account")
print("\n 22.   Login account")
print("\n 33.   Apply for a loan")
print("\n 44.   Apply for a credit card")
print("\n 55.   Apply for a debit card")
print("\n 66.   Apply for a new passbook")
print("\n 77.   Apply for a cheque book")

choice = int(input("\n ➡️   Enter your choice : "))


if choice == 11:
    print("\n 🔒----- Create Your Account ----- 🔒")
    print("\n ⚠️ !!!!! Enter Your Details !!!!! ⚠️")
    name = (input("\n 👤 Enter Your Full Name : ="))
    adhar = (input("\n 🆔 Enter your Adhar number := "))
    mobile = int(input("\n 📱 Enter your mobile number := "))
    email = (input("\n 📧  Enter your email address := "))
    password = int(input("\n 🔒 Create your password : = "))  
    print("\n ✅ Your account has been created successfully")
    
    
    accounn_no = 100000000000
    print("\n 💰 Your account details are:")
    print("\n 👤 Name  = ", name)
    print("\n 🆔 Adhar = ", adhar)
    print("\n 📱 Ph.no = ", mobile) 
    print("\n 📧 Email = ", email)
    print("\n 👤 Username := ", name)
    print("\n 🔒 Password := ", password)  # Fixed password display
    print("\n 🏦 Your account number is = ", accounn_no)
    print("\n ✅ Your account has been created successfully")
    print("\n 💰 Enter your default amount : =")
    
    amount = int(input("\n 💰 Enter your default amount : = "))
    print("\n 💰 Amount credited successfully := ", amount)
    exit()


#account login
elif choice == 22: 
   
    print("\n 🔒 ----- Login Your Account ----- 🔒")
    username = (input("\n 👤 Enter Username : "))
    password = (input("\n 🔑 Enter Password : ")) 
    if username != "vaibhavjaybhaye" or password != "999":
        print("\n ⚠️ !!!!! Invalid Username or Password !!!!! ⚠️")
        exit()
    else:
        balance = 10000
        print("\n ✅--------- Login successfull ---------✅")
        print("\n 💰 Your Current balance is = ", balance)
        print("\n ✅ You successfully logged in to your account")
             

        while True:
            
            print("\n 🏦 ***** Bank Account Management System ***** 🏦")
            print("\n 📋 Please select an option from the menu : ")
            print("\n 1. 💵 Deposit")
            print("\n 2. 💸 Withdraw")
            print("\n 3. ℹ️ Check Balance")
            print("\n 4. 👋 Exit")
            
            choice = int(input("\n ➡️ Enter your choice : "))
            
            if choice == 1:
                balance = deposit(balance)
            elif choice == 2:
                balance = withdraw(balance)
            elif choice == 3:
                check_balance(balance)
            elif choice == 4:
                exit()
                break
            else:
                print("\n ⚠️ Invalid choice please try again")
                print("\n 📋 Please select an option from the menu")

elif choice == 33:
    apply_loan()
    exit()

elif choice == 44:
    apply_credit_card()
    exit()

elif choice == 55:
    apply_debit_card()
    exit()

elif choice == 66:
    apply_passbook()
    exit()

elif choice == 77:
    apply_cheque_book()
    exit()

else:
    print("\n ⚠️ Invalid choice please try again")
    exit()
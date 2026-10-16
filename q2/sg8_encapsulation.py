class Bank_account: #initialize the variables.
  def __init__(self, account_number, balance):
    self.__account_number = account_number
    self.__balance = balance

#setter and getter methods for account number and balance.
  def set_account_number(self, account_number):
    self.__account_number = account_number

  def get_account_number(self):
    return self.__account_number

  def set_balance(self, balance):
    deposit = int(input("\nUpdate balance to ")) # input to change balance must not be less than zero
    if deposit > 0: #If deposit is less than zero then it is not recorded, for example (-100)
      self.__balance += deposit
    else:
      print("The balance must not be a negative number.")

  def get_balance(self):
    return self.__balance

a1 = Bank_account(12345,1000) #define the objects for the bank account
print("Account 1") 
print("Account Number:",a1.get_account_number())
print("Balance:",a1.get_balance())
a1.set_balance(1000)
print("Account Number:",a1.get_account_number())
print("Balance:",a1.get_balance())

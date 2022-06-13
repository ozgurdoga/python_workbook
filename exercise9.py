#Pretend that you have just opened a new savings account that earns 4 percent interest
#per year. The interest that you earn is paid at the end of the year, and is added
#to the balance of the savings account. Write a program that begins by reading the
#amount of money deposited into the account from the user. Then your program should
#compute and display the amount in the savings account after 1, 2, and 3 years. Display
#each amount so that it is rounded to 2 decimal places.

saving_account = int(input("Amount of Money Deposited Into the Account : "))
year_block = int(input("How many years = "))
def compute_account(total_money,year = 1):
    interest_percent = 4
    
    for _ in range(year):
        yearly_income = (total_money / 100) * interest_percent
        total_money += yearly_income
    return round(total_money,2)
print(compute_account(saving_account,1))
print(compute_account(saving_account,2))
print(compute_account(saving_account,year_block))

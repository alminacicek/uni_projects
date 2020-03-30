from bank_accounts import bank_account
account_001 = bank_account(1, "John Doe", 178293)
print(account_001.account_num)
print(account_001.account_owner)
print(account_001.amount)

account_001.withdraw(120)
print(account_001.amount)

account_001.deposit(789)
print(account_001.amount)
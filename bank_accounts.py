class bank_account():

    def __init__(self, account_num, account_owner, amount):
        self.account_num = account_num
        self.account_owner = account_owner
        self.amount = amount

    def withdraw(self, withdrawn):
        self.amount -= withdrawn

    def deposit(self, deposited):
        self.amount += deposited

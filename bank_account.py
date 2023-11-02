account_database = []

class Account:
    def __init__(self, num, type, name, init_balance):
        if self.search_account_db(num) == -1:
            self.account_number = num
            self.type = type
            self.account_name = name
            self.balance = init_balance
            account_database.append(self)
        else:
            print("Account", num, "already exists")

    def delete_account(self, num):
        index = self.search_account_db(num)
        if index != -1:
            print("Deleting account:", account_database[index].account_number)
            del account_database[index]
        else:
            print(num, "invalid account number; nothing to be deleted.")

    # returns the index of the account in the database
    def search_account_db(self, num):
        for i in range(len(account_database)):
            if account_database[i].account_number == num:
                return i
        return -1

    def deposit(self, account_num, amount):
        index = self.search_account_db(account_num)
        if index != -1:
            print("Depositing", amount, "to", account_database[index].account_number)
            account_database[index].balance += amount
        else:
            print(account_num, "invalid account number; no deposit action performed.")

    def withdraw(self, account_num, amount):
        index = self.search_account_db(account_num)
        if index != -1:
            if account_database[index].balance >= amount:
                print("Withdrawing", amount, "from", account_database[index].account_number)
                account_database[index].balance -= amount
            else:
                print("withdrawal amount", amount, "exceeds the balance of", account_database[index].balance,
                      "for", account_num, "account.")
        else:
            print(account_num, "invalid account number; no withdrawal action performed.")

    def show_account(self, account_num):
        index = self.search_account_db(account_num)
        if index != -1:
            print("Showing details for", account_database[index].account_number)
            print(account_database[index])
        else:
            print(account_num, "invalid account number; nothing to be shown for.")


account1 = Account("0000", "saving", "David Patterson", 1000)
account2 = Account("0001", "checking", "John Hennessy", 2000)
account3 = Account("0003", "saving", "Mark Hill", 3000)
account4 = Account("0004", "saving", "David Wood", 4000)
account5 = Account("0004", "saving", "David Wood", 4000)
print(account_database)

account3.show_account('0003')
account3.deposit('0003', 50)
account3.show_account('0003')
account3.withdraw('0003', 25)
account3.show_account('0003')
account3.delete_account('0003')
account3.show_account('0003')  # This will print that '0003' is an invalid account number
account3.deposit('0003', 50)  # This will print that '0003' is an invalid account number
account2.withdraw('0001', 6000)

# show_account('0003')
# deposit('0003', 50)
# show_account('0003')
# withdraw('0003', 25)
# show_account('0003')
# delete_account('0003')
# show_account('0003')
# deposit('0003', 50)
# withdraw('0001', 6000)

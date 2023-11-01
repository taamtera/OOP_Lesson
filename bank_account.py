class AccountDB:
    def __init__(self):
        self.account_database = []

    def __str__(self):
        s = ""
        for i in self.account_database:
            s += str(i) + ", "
        return s

    def __search_account_db(self, num):
        for i in range(len(self.account_database)):
            if self.account_database[i].account_number == num:
                return i
        return -1

    def insert(self, account):
        index = self.__search_account_db(account.account_number)
        if index == -1:
            self.account_database.append(account)
        else:
            print("Account", account.account_number, "already exists")

    def search(self, account_num):
        index = self.__search_account_db(account_num)
        if index != -1:
            return self.account_database[index]
        else:
            print("Account", account_num, "does not exist")
            return None

    def delete_account(self, num):
        index = self.__search_account_db(num)
        if index != -1:
            print("Deleting account:",
                  self.account_database[index].account_number)
            del self.account_database[index]
        else:
            print(num, "invalid account number; nothing to be deleted.")

    def deposit(self, account_num, amount):
        index = self.__search_account_db(account_num)
        if index != -1:
            print("Depositing", amount, "to",
                  self.account_database[index].account_number)
            self.account_database[index].deposit(amount)
        else:
            print(account_num, "invalid account number; no deposit action performed.")

    def withdraw(self, account_num, amount):
        index = self.__search_account_db(account_num)
        if index != -1:
            if self.account_database[index].balance >= amount:
                print("Withdrawing", amount, "from",
                      self.account_database[index].account_number)
                self.account_database[index].withdraw(amount)
            else:
                print("withdrawal amount", amount, "exceeds the balance of",
                      self.account_database[index].balance, "for", account_num, "account.")
        else:
            print(account_num, "invalid account number; no withdrawal action performed.")

    def show_account(self, account_num):
        index = self.__search_account_db(account_num)
        if index != -1:
            print("Showing details for",
                  self.account_database[index].account_number)
            print(self.account_database[index])
        else:
            print(account_num, "invalid account number; nothing to be shown for.")


class Account:

    def __init__(self, num, type, name, init_balance):
        self.account_number = num
        self.type = type
        self.account_name = name
        self.balance = init_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def __str__(self):
        return '{' + f"{self.account_number},{self.type},{self.account_name},{self.balance}" + '}'


a1 = Account("0000", "saving", "David Patterson", 1000)
a2 = Account("0001", "checking", "John Hennessy", 2000)
a3 = Account("0003", "saving", "Mark Hill", 3000)
a4 = Account("0004", "saving", "David Wood", 4000)
a5 = Account("0004", "saving", "David Wood", 4000)
my_account_db = AccountDB()
my_account_db.insert(a1)
my_account_db.insert(a2)
my_account_db.insert(a3)
my_account_db.insert(a4)
my_account_db.insert(a5)
print(my_account_db)
my_account_db.search('0003').deposit(50)
print(my_account_db)

# create_account("0000", "saving", "David Patterson", 1000)
# create_account("0001", "checking", "John Hennessy", 2000)
# create_account("0003", "saving", "Mark Hill", 3000).
# create_account("0004", "saving", "David Wood", 4000)
# create_account("0004", "saving", "David Wood", 4000)
# print(account_database)
# show_account('0003')
# deposit('0003', 50)
# show_account('0003')
# withdraw('0003', 25)
# show_account('0003')
# delete_account('0003')
# show_account('0003')
# deposit('0003', 50)
# withdraw('0001', 6000)

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

    def search_public(self, account_num):
        index = self.__search_account_db(account_num)
        if index != -1:
            return self.account_database[index]
        else:
            print("Account", account_num, "does not exist")
            return None

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


account1 = Account("0000", "saving", "David Patterson", 1000)
account2 = Account("0001", "checking", "John Hennessy", 2000)
account3 = Account("0003", "saving", "Mark Hill", 3000)
account4 = Account("0004", "saving", "David Wood", 4000)
account5 = Account("0004", "saving", "David Wood", 4000)
my_account_DB = AccountDB()
my_account_DB.insert(account1)
my_account_DB.insert(account2)
my_account_DB.insert(account3)
my_account_DB.insert(account4)
my_account_DB.insert(account5)
print(my_account_DB)
my_account_DB.search_public("0003").deposit(50)
print(my_account_DB)
my_account_DB.search_public("0003").withdraw(100)
print(my_account_DB)

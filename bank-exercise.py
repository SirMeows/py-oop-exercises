class Bank:

    def __init__(self):
        self.accounts = []

    def add_accounts(self, *args):
        for i in args:
            self.accounts.append(i)

class Account:
    
    def __init__(self, account_nr, customer):
        self.account_nr = account_nr
        if type(customer) == Customer:
            self.customer = customer

    def print_account_nr(self):
        return f'account nr: { self.account_nr }'


class Customer:

    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id

    def __str__(self): # prints a string (user friendly)
        return f'name: {self.name}, customer_id: {self.customer_id}'

    def __repr__(self): # prints a dictionary (developer friendly)
        return f'name: {self.name}, customer_id: {self.customer_id}'

bank_1 = Bank()
print(bank_1)

customer_1 = Customer('Arael', 1)

account_1 = Account(12345, customer_1)
account_2 = Account(56789, Customer('Xatana', 2))

bank_1.add_accounts(account_1, account_2)

account_1.print_account_nr

print(customer_1)
print(account_2.customer.name)






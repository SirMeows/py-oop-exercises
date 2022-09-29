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
        print(f'account nr: { self.account_nr }')


class Customer:

    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id

    def __str__(self):
        return f'name: {self.name}, customer_id: {self.customer_id}'

    def __repr__(self):
        return f'Customer("{ self.name }", {self.customer_id})'

bank_1 = Bank()

customer_1 = Customer('Arael', 1)
customer_2 = Customer('Xatana', 2)

account_1 = Account(12345, customer_1)
account_2 = Account(56789, customer_2)

bank_1.add_accounts(account_1, account_2)

account_1.print_account_nr()

print(customer_1) # calls __str__
print(repr(customer_1)) # string representation of the object
print(eval(repr(customer_1))) # new object 
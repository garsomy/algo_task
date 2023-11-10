class Bank:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transaction = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction.append(f'Пополнение счёта на сумму: {amount}')

    def withdrawal(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction.append(f'Снятие счёта на сумму: {amount}')

    def get_balance(self):
        return self.balance

    def get_transaction(self):
        return self.transaction


b = Bank('Васильев Вася')
print('Клиент:', b.name)
print('Начальный баланс:', b.get_balance())

b.deposit(10000)
b.withdrawal(500)
b.withdrawal(1500)

print('\nТранзакции по счету:')

for transaction in b.get_transaction():
    print(transaction)

print('\nОкончательный баланс:', b.get_balance())
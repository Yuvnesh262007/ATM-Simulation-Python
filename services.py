import models

def check_balance():
    return models.balance

def deposit(amount):
    models.balance += amount
    models.transactions.append(f"Deposited: {amount}")

def withdraw(amount):
    if amount <= models.balance:
        models.balance -= amount
        models.transactions.append(f"Withdrawn: {amount}")
        return True
    return False

def get_statement():
    return models.transactions
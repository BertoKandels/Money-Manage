from datetime import datetime, date

from peewee import *

db = SqliteDatabase('expenses.db')

class Expense():
    def __init__(self, name, amount, due_date):
        self.amount = amount
        self.due_date = due_date
        self.name = name


def calc_days_till_due_date(due_date):
    now = datetime.now()
    delta = due_date.day - now.day
    if delta >= 0:
        print(delta)
    else:
        print("Expense needs to updated Date")


dueDate = date(2020, 4, 24)
expense = Expense("Phone", 100, dueDate)

calc_days_till_due_date(expense.due_date)

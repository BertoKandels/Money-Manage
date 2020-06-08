from peewee import *
from collections import OrderedDict

from datetime import datetime, date


import re
import sys
import os

db = SqliteDatabase('expenses.db')


class Expense(Model):
    name = TextField()
    due_date = DateTimeField()
    amount = TextField()

    class Meta:
        database = db

def initialize():
    """Create the database and the table"""
    db.connect()
    db.create_tables([Expense], safe=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_loop():
    """Show the menu"""
    choice = None

    while choice != 'q':
        clear()
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower().strip()

        if choice in menu:
            clear()
            menu[choice]()

def add_expense():
    """ Add an expense"""
    print("Adding a new Expense. ")
    name = input("Enter expense name. ")
    amount = int(input("Enter amount due. "))
    due_date = input("Enter Upcoming Due Date. 'ex. yyyy-mm-dd ")

    dateArray = [due_date.split('-')]
    year1 = int(dateArray[0][0])
    month1 = int(dateArray[0][1])
    day1 = int(dateArray[0][2])

    dueDate = date(year=year1, month=month1, day=day1)
    print("Name:\{name} Amount: \{amount} DueDate: |{dueDate}")

    if input("Save Entry?: [Yn] ").lower() != 'n':
        Expense.create(name=name, amount=amount, due_date=dueDate)
        print("Save Successfully!")







def view_expenses(search_query=None):

    expenses = Expense.select().order_by(Expense.due_date.desc())
    if search_query:
        expenses = expenses.where(Expense.name.contains(search_query))

    for expense in expenses:
        timestamp = expense.due_date.strftime('%A %b %d')
        clear()
        print(timestamp)
        print('='*len(timestamp))
        print(expense.name)
        print("$" + expense.amount)
        print("Due Date:" + timestamp)
        print('\n\n'+'='*len(timestamp))
        print('n) for next entry')
        print('d) delete entry')
        print('q) return to main menu')

        next_action = input('Action: [Ndq] '.lower().strip())
        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_expense(expense)


def search_expenses():
    view_expenses(input('search query: '))

def delete_expense(expense):
    if input("are you sure? [yN] ").lower() == 'y':
        expense.delete_instance()
        print("Expense Deleted!")




menu = OrderedDict([
    ('a', add_expense),
    ('v', view_expenses),
    ('s', search_expenses)
])

if __name__ == '__main__':
    initialize()
    menu_loop()
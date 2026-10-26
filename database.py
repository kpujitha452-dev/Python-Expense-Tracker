

import sqlite3

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))

    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses (name, amount) VALUES (?, ?)",
        (name, amount)
    )

    conn.commit()
    conn.close()

    print("Expense saved successfully!")

def view_expenses():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    for expense in expenses:
        print(expense[1], "-", expense[2])

    conn.close()

def calculate_total():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]

    print("Total expenses:", total if total else 0)

    conn.close()

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        calculate_total()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")

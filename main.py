import csv
import os

FILE_NAME = "expenses.csv"
transactions = []
monthly_budget = 0


def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(row)


def save_data():
    with open(FILE_NAME, "w", newline="") as file:
        fields = ["type", "category", "amount", "description"]
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(transactions)


def add_income():
    amount = float(input("Enter income amount: "))
    description = input("Enter income source: ")

    transactions.append({
        "type": "Income",
        "category": "Income",
        "amount": amount,
        "description": description
    })

    save_data()
    print("Income added successfully!")


def add_expense():
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    description = input("Enter description: ")

    transactions.append({
        "type": "Expense",
        "category": category,
        "amount": amount,
        "description": description
    })

    save_data()
    print("Expense added successfully!")


def view_transactions():
    if not transactions:
        print("No transactions found.")
        return

    print("\n--- TRANSACTION HISTORY ---")

    for t in transactions:
        print(
            t["type"], "|",
            t["category"], "|",
            t["amount"], "|",
            t["description"]
        )


def calculate_balance():
    income = 0
    expenses = 0

    for t in transactions:
        amount = float(t["amount"])

        if t["type"] == "Income":
            income += amount
        else:
            expenses += amount

    print("\nTotal Income:", income)
    print("Total Expenses:", expenses)
    print("Remaining Balance:", income - expenses)


def set_budget():
    global monthly_budget
    monthly_budget = float(input("Enter your monthly budget: "))
    print("Budget set successfully!")


def budget_analysis():
    total_expenses = 0

    for t in transactions:
        if t["type"] == "Expense":
            total_expenses += float(t["amount"])

    print("\nMonthly Budget:", monthly_budget)
    print("Total Expenses:", total_expenses)

    if monthly_budget == 0:
        print("Please set your budget first.")
    elif total_expenses > monthly_budget:
        print("Warning! You have exceeded your budget.")
    else:
        remaining = monthly_budget - total_expenses
        print("Budget remaining:", remaining)


def category_analysis():
    categories = {}

    for t in transactions:
        if t["type"] == "Expense":
            category = t["category"]
            amount = float(t["amount"])

            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

    print("\n--- CATEGORY-WISE EXPENSES ---")

    if not categories:
        print("No expenses available.")
    else:
        for category, amount in categories.items():
            print(category, ":", amount)


def main():
    load_data()
    while True:
        print("\n===== PERSONAL EXPENSE & BUDGET ANALYZER =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Calculate Balance")
        print("5. Set Budget")
        print("6. Budget Analysis")
        print("7. Category Analysis")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_transactions()
        elif choice == "4":
            calculate_balance()
        elif choice == "5":
            set_budget()
        elif choice == "6":
            budget_analysis()
        elif choice == "7":
            category_analysis()
        elif choice == "8":
            save_data()
            print("Thank you for using Expense Analyzer!")
            break
        else:
            print("Invalid choice. Please try again.")
print("Project Started")
main()

# SECTION 0 – IMPORTS & REGEX
"""
Expense Tracker

A command-line program for recording and managing expense entries.
Stores each expense in a text file and allows searching, listing,
and computing totals by category or date.
"""

import re
from datetime import datetime
import os

# File to store all expense records
DATA_FILE = "expenses.txt"

# Date format: dd/mm/yyyy
DATE_PATTERN = re.compile(r'^(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/\d{4}$')

# Valid amounts: integers or decimals up to 2 digits
AMOUNT_PATTERN = re.compile(r'^[0-9]+(\.[0-9]{1,2})?$')
# ----------------

# SECTION 1 – USER INPUT FUNCTIONS
# (Add functions to take validated user input: date, amount, text, etc.)
# Input validation helpers
# --------------------------

def ask_date(prompt="Enter date (dd/mm/yyyy): "):
    """Prompt user for a valid date in dd/mm/yyyy format."""
    while True:
        text = input(prompt).strip()

        if DATE_PATTERN.match(text):
            try:
                datetime.strptime(text, "%d/%m/%Y")
                return text
            except ValueError:
                print("Invalid date. Try again.")
        else:
            print("Use dd/mm/yyyy format.")


def ask_amount(prompt="Enter amount: "):
    """Prompt user for a positive amount (supports two decimals)."""
    while True:
        text = input(prompt).strip()

        if AMOUNT_PATTERN.match(text):
            amt = float(text)
            if amt > 0:
                return round(amt, 2)
            print("Amount must be greater than 0.")
        else:
            print("Enter a valid number (e.g., 120 or 120.50).")


def ask_text(prompt):
    """Prompt user for non-empty text."""
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("This field cannot be empty.")


# --------------------------


# SECTION 2 – FILE HANDLING
# (Add load and save functions for working with the data file)
# File operations

def load_expenses():
    """Load all expense records from the file."""
    expenses = []

    if not os.path.isfile(DATA_FILE):
        return expenses

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split("|")
            if len(parts) < 5:
                continue

            try:
                expense = {
                    "id": int(parts[0]),
                    "date": parts[1],
                    "amount": float(parts[2]),
                    "category": parts[3],
                    "description": "|".join(parts[4:])
                }
                expenses.append(expense)
            except ValueError:
                continue

    return expenses


def save_expenses(expenses):
    """Write all expense records back to the file."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        for e in expenses:
            line = (
                f"{e['id']}|"
                f"{e['date']}|"
                f"{e['amount']:.2f}|"
                f"{e['category'].replace('|','/')}|"
                f"{e['description'].replace('|','/')}\n"
            )
            file.write(line)
    file.close()


# --------------------------
# Core operations

def next_id(expenses):
    """Return the next available numeric ID."""
    if not expenses:
        return 1
    return max(e["id"] for e in expenses) + 1

# --------------------------


# SECTION 3 – CORE OPERATION 1
# add_expense()- pavan kumar



# SECTION 4 – CORE OPERATION 2
# list_all(), list_by_date(), list_by_category()- Jyothi basu and akshay raju

#List all expenses

def list_all(expenses):
    """Display all expenses sorted by date and ID."""
    if not expenses:
        print("\nNo expenses recorded.")
        return

    print("\nAll Expenses:")

    sorted_exp = sorted(
        expenses,
        key=lambda e: (datetime.strptime(e["date"], "%d/%m/%Y"), e["id"])
    )

    for e in sorted_exp:
        print(
            f"ID: {e['id']} | Date: {e['date']} | Amount: {e['amount']:.2f} | "
            f"Category: {e['category']} | Description: {e['description']}"
        )


# list_by_date()
def list_by_date(expenses):
    """Display expenses for a specific date."""
    date = ask_date("Enter date to search: ")

    filtered_expenses_list = []

    for e in expenses:
        if e["date"] == date:
            filtered_expenses_list.append(e)

    if not filtered_expenses_list:
        print("No expenses found on this date.")
        return

    else:
        print("Expenses on the ", date, ": ")

        for f in filtered_expenses_list:
            print("ID: ", f['id'], " | Amount: ", f['amount'], " | Category: ", f['category'], " | Description: ", f['description'])

# list_by_category()
def list_by_category(expenses):
    """Display expenses belonging to a category."""
    cat = ask_text("Enter category: ").lower()
    filtered_list = []

    for e in expenses:
        if e["category"].lower() == cat:
            filtered_list.append(e)

    if not filtered_list:
        print("No expenses found for this category.")
        return
    else:
        print("Expenses in this ", cat, ": ")

    for f in filtered_list:
        print("ID: ", f['id'], " | Date: ", f['date'], " | Amount: ", f['amount'], " | Description: ", f['description'])

# SECTION 5 – CORE OPERATION 3
# total_amount(), total_by_category()- chandan
def total_by_category(expenses):
    """Compute and display totals for each category."""
    if not expenses:
        print("No expenses yet.")
        return

    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]

    print("\nTotal By Category:")
    for cat, total in totals.items():
        print(f"{cat}: {total:.2f}")


def total_amount(expenses):
    """Display total amount of all expenses."""
    total = sum(e["amount"] for e in expenses)
    print("\nTotal Amount Spent:", f"{total:.2f}")



# SECTION 6 – CORE OPERATION 4    # delete_expense(), update_expense()
def delete_by_id(expenses):
    """Remove an expense using its ID."""
    id_text = ask_text("Enter ID to delete: ")

    try:
        target = int(id_text)
    except ValueError:
        print("Invalid ID format.")
        return

    before = len(expenses)
    expenses[:] = [e for e in expenses if e["id"] != target]

    if len(expenses) < before:
        save_expenses(expenses)
        print("Expense deleted.")
    else:
        print("ID not found.")



# SECTION 7 – MAIN FUNCTION
# (Add menu, routing to different operations, and program start)
def main_menu():
    expenses = load_expenses()
    print("Welcome to Expense Tracker")

    while True:
        print("\nMenu:")
        print("1. Add Expense")
        print("2. List All")
        print("3. List by Date")
        print("4. List by Category")
        print("5. Total by Category")
        print("6. Total Amount")
        print("7. Delete by ID")
        print("8. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_all(expenses)
        elif choice == "3":
            list_by_date(expenses)
        elif choice == "4":
            list_by_category(expenses)
        elif choice == "5":
            total_by_category(expenses)
        elif choice == "6":
            total_amount(expenses)
        elif choice == "7":
            delete_by_id(expenses)
        elif choice == "8":
            print("Goodbye.")
            break
        else:
            print("Enter a number between 1 and 8.")


# --------------------------
# Entry point
# --------------------------

if __name__ == "__main__":
    main_menu()



# END OF PROJECT SKELETON

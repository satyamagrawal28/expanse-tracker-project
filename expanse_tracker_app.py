
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



# SECTION 3 – CORE OPERATION 1
# add_expense()



# SECTION 4 – CORE OPERATION 2
# list_all(), list_by_date(), list_by_category()



# SECTION 5 – CORE OPERATION 3
# total_amount(), total_by_category()



# SECTION 6 – CORE OPERATION 4
# delete_expense(), update_expense()



# SECTION 7 – MAIN FUNCTION
# (Add menu, routing to different operations, and program start)



# END OF PROJECT SKELETON


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

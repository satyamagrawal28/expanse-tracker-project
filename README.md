# Expense Tracker (CLI – Python Fundamentals Team Project)

## Overview

Expense Tracker is a command-line application developed using Python.

It allows users to record, view, and manage daily expenses using file-based storage.

This project was developed as a team assignment for a Python Fundamentals course. The primary objective was to practice modular programming, input validation, and file handling.

## Features

- Add a new expense:
  - Date in dd/mm/yyyy format
  - Amount (positive number with up to two decimal places)
  - Category
  - Description

- List all expenses (sorted by date and ID)

- Filter expenses:
  - By date
  - By category

- View:
  - Total amount spent
  - Total by category

- Delete expense by ID

All expense records are stored in a structured text file named expenses.txt.

## Technologies Used

- Python 3
- Regular Expressions (re module)
- File handling
- datetime module
- Command-line interface (CLI)

No external libraries were used.

## Project Structure

The repository contains the following files:

- expense-tracker.py  
  Main Python script containing all program logic and functions.

- expenses.txt  
  Data file where all expense records are stored.  
  This file is created automatically when the first expense is added.

- README.md  
  Project documentation and usage instructions.

## How to Run

1. Make sure Python 3 is installed on your system.

2. Clone the repository:
   git clone <repository-link>

3. Navigate into the project directory:
   cd expense-tracker

4. Run the program:
   python expense-tracker.py

## Team Members

- Satyamagrawal – Team Lead
- Pavan Kumar – Add Expense
- Akshaya Raju – List All
- Jyothi Basu – List by Date, List by Category
- Chandan – Totals and Calculations

## Academic Context

This project was completed as part of a Python Fundamentals course to demonstrate understanding of:

- Function-based program design
- Data validation
- File-based data persistence
- Sorting and filtering structured data
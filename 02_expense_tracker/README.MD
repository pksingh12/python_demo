expense_tracker/
│── main.py                # Entry point
│── expense_manager/        # Package for business logic
│   │── __init__.py         # Makes it a package
│   │── expenses.py         # Handles expense operations
│   │── storage.py          # Handles file storage
│── requirements.txt        # Dependencies (if needed)
│── README.md               # Documentation
│── expenses.csv            # File to store expense data


# Expense Tracker

A simple command-line expense tracker that allows users to record expenses, view all expenses, and filter expenses by category.

## Features
- Add an expense (amount, category, date).
- View all recorded expenses.
- Filter expenses by category.
- Store expenses in a CSV file.

## How to Run
```sh
python3 main.py

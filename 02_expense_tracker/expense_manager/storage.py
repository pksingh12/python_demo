import csv
import os

class ExpenseStorage:
    FILENAME = "expenses.csv"

    @staticmethod
    def saveExpenses(expenses):
        with open(ExpenseStorage.FILENAME,mode="w",newline="") as file:
            writer = csv.writer(file)
            writer.writerow([ "Amount","Category","Date"])
            for exp in expenses:
                writer.writerow([exp.amount, exp.category, exp.date])

    
    @staticmethod
    def loadExpenses(expense_manager):
        if not os.path.exists(ExpenseStorage.FILENAME):
            return
        
        with open(ExpenseStorage.FILENAME,mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expense_manager.add_expense(float(row["Amount"]), row["Category"])

            
    
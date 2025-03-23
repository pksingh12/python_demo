import datetime

class Expense:
    def __init__(self,amount,category,date = None):
        self.category = category
        self.amount = amount
        self.date = date if date else datetime.date.today()
    
    def create_dict(self):
        return {  "amount": self.amount,"category": self.category, "date": self.date.strftime("%Y-%m-%d") }
    
class ExpenseManager:
    def __init__(self):
        self.expenses = []
    
    def add_expense(self,amount,category):
        new_expense = Expense(amount,category)
        self.expenses.append(new_expense)
        return new_expense
    
    def get_expenses(self,category=None):
        if category:
            return [exp for exp in self.expenses if exp.category == category]
        return self.expenses
     

    


    

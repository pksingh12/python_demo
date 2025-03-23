from expense_manager.expenses import ExpenseManager
from expense_manager.storage import ExpenseStorage

def main():

    expense_manager = ExpenseManager()
    ExpenseStorage.loadExpenses(expense_manager)

    while True:

        print("\n Expense Tracker Menu: ")
        print("1. Add Expense")
        print("2. View All Expense")
        print("3. View Expenses By Category")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter expense amount: "))
            category = input("Enter category: ")
            expense_manager.add_expense(amount,category)
            ExpenseStorage.saveExpenses(expense_manager.expenses)
            print("Expense added sucessfully")

        elif choice == "2":
            my_expenses = expense_manager.get_expenses()
            for exp in my_expenses:
                print(f"{exp.date} - {exp.category}: {exp.amount}")

        elif choice == "3":
            category = input("Enter category: ")
            filtered_expenses = expense_manager.get_expenses(category)
            if not filtered_expenses:
                print("No Expenses Found")
            
            for exp in filtered_expenses:
                print(f"{exp.date} - {exp.category}: ${exp.amount}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()        







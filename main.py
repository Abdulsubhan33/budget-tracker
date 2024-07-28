import json

DATA_FILE = 'budget.json'

def load_data():
    """Load budget data from a JSON file"""
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {'income': 0, 'expenses': 0, 'balance': 0}

def save_data(data):
    """Save budget data to a JSON file"""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_income(amount):
    """Add income to the budget."""
    data = load_data()
    if amount < 0:
        print("Income amount must be positive.")
        return
    data['income'] += amount
    # Recalculate balance
    data['balance'] = data['income'] - data['expenses']
    save_data(data)

def add_expense(amount):
    """Add expense to the budget."""
    data = load_data()
    if amount < 0:
        print("Expense amount must be positive.")
        return
    data['expenses'] += amount
    # Recalculate balance
    data['balance'] = data['income'] - data['expenses']
    save_data(data)

def show_summary():
    """Show current budget summary"""
    data = load_data()
    print(f"Income: ${data['income']:.2f}")
    print(f"Expenses: ${data['expenses']:.2f}")
    print(f"Balance: ${data['balance']:.2f}")

def main():
    while True:
        print("\nPersonal Budget Tracker")
        print("1. Add Income")
        print("2. Add Expenses")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            try:
                amount = float(input("Enter income amount: $"))
                add_income(amount)
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
        elif choice == '2':
            try:
                amount = float(input("Enter expenses amount: $"))
                add_expense(amount)
            except ValueError:
                print("Invalid input. Please enter a numerical value.")
        elif choice == '3':
            show_summary()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()



import csv
from datetime import datetime
DATA_FILE = 'data.csv'

def init_csv():
    try:
        with open(DATA_FILE, mode='x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Type', 'Category', 'Amount', 'Note'])
    except FileExistsError:
        pass  

def add_transaction():
    t_type = input("Type (Income/Expense): ").strip().title()
    category = input("Category (e.g., Salary, Food, Rent): ").strip().title()
    amount = float(input("Amount: ₹"))
    note = input("Note (optional): ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, t_type, category, amount, note])
    print(" Transaction added!")


def view_summary():
    income = 0
    expense = 0
    with open(DATA_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            amt = float(row['Amount'])
            if row['Type'] == 'Income':
                income += amt
            elif row['Type'] == 'Expense':
                expense += amt
    balance = income - expense
    print("\n Summary:")
    print(f"Total Income: ₹{income}")
    print(f"Total Expense: ₹{expense}")
    print(f"Balance: ₹{balance}")


def show_all():
    print("\n🧾 All Transactions:")
    with open(DATA_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def main():
    init_csv()
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Transaction")
        print("2. View Summary")
        print("3. Show All Transactions")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            show_all()
        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()

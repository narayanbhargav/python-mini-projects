import sqlite3
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create a database or connect to an existing one
conn = sqlite3.connect('finance_tracker.db')
cursor = conn.cursor()

# Create a table to store transactions
cursor.execute('''CREATE TABLE IF NOT EXISTS transactions
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT, description TEXT, amount REAL)''')
conn.commit()

# Function to insert a transaction into the database
def insert_transaction():
    date = entry_date.get()
    description = entry_description.get()
    amount = float(entry_amount.get())

    cursor.execute("INSERT INTO transactions (date, description, amount) VALUES (?, ?, ?)", (date, description, amount))
    conn.commit()
    messagebox.showinfo("Success", "Transaction added successfully!")

# Function to show total amount spent
def show_total_spent():
    cursor.execute("SELECT SUM(amount) FROM transactions")
    total_spent = cursor.fetchone()[0]
    messagebox.showinfo("Total Amount Spent", f"You have spent a total of ${total_spent:.2f}")

# Function to show spending and income chart
def show_chart():
    cursor.execute("SELECT SUM(amount) FROM transactions")
    total_spent = cursor.fetchone()[0]
    income = float(entry_income.get())
    savings_goal = float(entry_savings_goal.get())
    
    labels = ['Spent', 'Income', 'Savings Goal']
    values = [total_spent, income, savings_goal]
    
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    canvas = FigureCanvasTkAgg(fig, master=app)
    canvas.get_tk_widget().grid(row=7, columnspan=2)

# Create the main application window
app = tk.Tk()
app.title("Finance Tracker")

# Create and place labels and entry fields
label_date = tk.Label(app, text="Date:")
entry_date = tk.Entry(app)
label_description = tk.Label(app, text="Description:")
entry_description = tk.Entry(app)
label_amount = tk.Label(app, text="Amount:")
entry_amount = tk.Entry(app)
button_add = tk.Button(app, text="Add Transaction", command=insert_transaction)
button_total_spent = tk.Button(app, text="Show Total Spent", command=show_total_spent)

# Create and place labels and entry fields for income and savings goal
label_income = tk.Label(app, text="Income:")
entry_income = tk.Entry(app)
label_savings_goal = tk.Label(app, text="Savings Goal:")
entry_savings_goal = tk.Entry(app)

# Create and place a button to show the chart
button_show_chart = tk.Button(app, text="Show Chart", command=show_chart)

# Layout using grid
label_date.grid(row=0, column=0)
entry_date.grid(row=0, column=1)
label_description.grid(row=1, column=0)
entry_description.grid(row=1, column=1)
label_amount.grid(row=2, column=0)
entry_amount.grid(row=2, column=1)
button_add.grid(row=3, columnspan=2)
button_total_spent.grid(row=4, columnspan=2)

label_income.grid(row=5, column=0)
entry_income.grid(row=5, column=1)
label_savings_goal.grid(row=6, column=0)
entry_savings_goal.grid(row=6, column=1)
button_show_chart.grid(row=7, columnspan=2)

# Start the main application loop
app.mainloop()

# Close the database connection when the application is closed
conn.close()
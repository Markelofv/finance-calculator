import tkinter as tk
from tkinter import messagebox


class FinanceCalculator:
    def reset(self):
        self.balance = 0.0
        self.transactions.clear()
    def reset(self):
        """Сбрасывает баланс и очищает историю операций."""
        self.balance = 0.0
        self.transactions.clear()
    def __init__(self):
        self.balance = 0.0
        self.transactions = []

    def add_income(self, amount, description="Income"):
        if amount <= 0:
            raise ValueError("Income must be greater than zero.")
        self.balance += amount
        self.transactions.append((description, amount))

    def add_expense(self, amount, description="Expense"):
        if amount <= 0:
            raise ValueError("Expense must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self.transactions.append((description, -amount))

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return list(self.transactions)


class FinanceCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Finance Calculator")
        self.calculator = FinanceCalculator()

        tk.Label(root, text="Число:").pack()
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        tk.Label(root, text="Описание:").pack()
        self.description_entry = tk.Entry(root)
        self.description_entry.pack()

        tk.Button(root, text="Сброс", command=self.reset_calculator).pack(fill="x")
        tk.Button(root, text="Добавить доход", command=self.add_income).pack(fill="x")
        tk.Button(root, text="Добавить расход", command=self.add_expense).pack(fill="x")
        tk.Button(root, text="Баланс", command=self.show_balance).pack(fill="x")
        tk.Button(root, text="История операций", command=self.show_transactions).pack(fill="x")

    def reset_calculator(self):
        self.calculator.reset()
        self.amount_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        messagebox.showinfo("Сброс", "Данные успешно сброшены!")

    def add_income(self):
        try:
            amount = float(self.amount_entry.get())
            description = self.description_entry.get() or "Баланс"
            self.calculator.add_income(amount, description)
            messagebox.showinfo("Выполнено!", "Доход добавлен!")
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def add_expense(self):
        try:
            amount = float(self.amount_entry.get())
            description = self.description_entry.get() or "Расход"
            self.calculator.add_expense(amount, description)
            messagebox.showinfo("Выполнено!", "Расход добавлен!")
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def show_balance(self):
        balance = self.calculator.get_balance()
        messagebox.showinfo("Баланс", f"Ваш баланс: {balance:.2f}")

    def show_transactions(self):
        transactions = self.calculator.get_transactions()
        text = "\n".join(f"{desc}: {amt:.2f}" for desc, amt in transactions)
        messagebox.showinfo("Операции", text or "Нет операций")


if __name__ == "__main__":
    root = tk.Tk()
    FinanceCalculatorApp(root)
    root.mainloop()
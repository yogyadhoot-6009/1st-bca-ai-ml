import tkinter as tk
pin = 8009
balance = 25900
attempts_left = 3

def atm():
    global attempts_left, balance

    # If card already blocked
    if attempts_left == 0:
        result_label.config(text="Card Blocked! No attempts left.", fg="red")
        submit_btn.config(state="disabled")
        return

    try:
        entered_pin = int(entry_pin.get())
        withdraw_amt = int(entry_amount.get())
    except ValueError:
        result_label.config(text="Enter valid numbers", fg="red")
        return

    # Check PIN
    if entered_pin == pin:
        # Check balance
        if withdraw_amt <= balance:
            balance -= withdraw_amt
            result_label.config(
                text=f" Withdrawal Successful\nRemaining Balance: ₹{balance}",
                fg="green"
            )
        else:
            result_label.config(
                text=f" Insufficient Balance\nCurrent Balance: ₹{balance}",
                fg="orange"
            )
    else:
        attempts_left -= 1
        result_label.config(
            text=f" Wrong PIN - Attempts left: {attempts_left}",
            fg="red"
        )
    if attempts_left == 0:
            result_label.config(text="Card Blocked! No attempts left.", fg="red")
            submit_btn.config(state="disabled")

# GUI
root = tk.Tk()
root.title("ATM System")
root.geometry("400x400")

tk.Label(root, text="ATM Machine", font=("Arial", 18, "bold")).pack()

tk.Label(root, text="Enter PIN:").pack()
entry_pin = tk.Entry(root, show="*", width=30)
entry_pin.pack()

tk.Label(root, text="Enter Withdraw Amount:").pack()
entry_amount = tk.Entry(root, width=30)
entry_amount.pack()

submit_btn = tk.Button(root, text="Submit", command=atm, width=15, bg="green", fg="white")
submit_btn.pack()

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

root.mainloop()
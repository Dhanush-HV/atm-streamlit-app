import streamlit as st

class BankAccount:
    def __init__(self, balance=0, pin="0000", account_type="Savings"):
        self.balance = balance
        self.pin = pin
        self.account_type = account_type

    def check_pin(self, entered_pin):
        return self.pin == entered_pin

    def withdraw(self, amount):
        if amount > self.balance:
            return "❌ Insufficient Balance"
        self.balance -= amount
        return f"✅ Withdrawn ₹{amount}. New Balance: ₹{self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"✅ Deposited ₹{amount}. New Balance: ₹{self.balance}"

    def check_balance(self):
        return f"💰 Current Balance: ₹{self.balance}"

st.title("🏧 ATM Banking System")

# Session state for persistent account
if "account" not in st.session_state:
    st.session_state.account = BankAccount(balance=5000, pin="4020")

menu = st.sidebar.selectbox("Menu", ["Enter PIN", "Withdraw", "Deposit", "Check Balance"])

# PIN CHECK
if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False

if menu == "Enter PIN":
    pin = st.text_input("Enter PIN", type="password")
    if st.button("Submit PIN"):
        if st.session_state.account.check_pin(pin):
            st.session_state.is_logged_in = True
            st.success("PIN Verified. You can use the ATM now!")
        else:
            st.error("Invalid PIN")

if st.session_state.is_logged_in:
    if menu == "Withdraw":
        amt = st.number_input("Enter amount to withdraw", min_value=1)
        if st.button("Withdraw"):
            st.write(st.session_state.account.withdraw(amt))

    elif menu == "Deposit":
        amt = st.number_input("Enter amount to deposit", min_value=1)
        if st.button("Deposit"):
            st.write(st.session_state.account.deposit(amt))

    elif menu == "Check Balance":
        st.write(st.session_state.account.check_balance())

else:
    st.warning("Please verify PIN first from the menu.")

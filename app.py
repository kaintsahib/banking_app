import streamlit as st
from core.account import Account
from services.transaction_service import TransactionService


if 'acc1' not in st.session_state:
    st.session_state.acc1 = Account("Gaurav", 1000)

if 'acc2' not in st.session_state:
    st.session_state.acc2 = Account("Investor", 500)

service = TransactionService()

st.title("Simple Banking App")

# Show balances
st.write(f"### Balance of {st.session_state.acc1._owner}: ₹{st.session_state.acc1.balance}")
st.write(f"### Balance of {st.session_state.acc2._owner}: ₹{st.session_state.acc2.balance}")

# Deposit to Account 1
deposit_amount = st.number_input(f"Deposit amount to {st.session_state.acc1._owner}", min_value=0.0, step=100.0)
if st.button(f"Deposit to {st.session_state.acc1._owner}"):
    if deposit_amount > 0:
        st.session_state.acc1.deposit(deposit_amount)
        st.success(f"Deposited ₹{deposit_amount} to {st.session_state.acc1._owner}")

# Withdraw from Account 2
withdraw_amount = st.number_input(f"Withdraw amount from {st.session_state.acc2._owner}", min_value=0.0, step=100.0)
if st.button(f"Withdraw from {st.session_state.acc2._owner}"):
    try:
        st.session_state.acc2.withdraw(withdraw_amount)
        st.success(f"Withdrawn ₹{withdraw_amount} from {st.session_state.acc2._owner}")
    except Exception as e:
        st.error(str(e))

# Transfer from Account 1 to Account 2
transfer_amount = st.number_input("Transfer amount from Gaurav to Investor", min_value=0.0, step=100.0)
if st.button("Transfer"):
    try:
        service.transfer(st.session_state.acc1, st.session_state.acc2, transfer_amount)
        st.success(f"Transferred ₹{transfer_amount} from {st.session_state.acc1._owner} to {st.session_state.acc2._owner}")
    except Exception as e:
        st.error(str(e))

# Show transactions of both accounts
if st.checkbox("Show transactions"):
    st.write(f"**Transactions of {st.session_state.acc1._owner}:**")
    for t in st.session_state.acc1.get_transactions():
        st.write(t)

    st.write(f"**Transactions of {st.session_state.acc2._owner}:**")
    for t in st.session_state.acc2.get_transactions():
        st.write(t)

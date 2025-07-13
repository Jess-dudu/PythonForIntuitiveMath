import streamlit as st

st.title("Loan/Mortgage Calculator")

home_price = st.number_input("Home Price ($)", min_value=0.0, value=300000.0, step=1000.0)

down_type = st.radio("Down Payment Type", ["Percentage (%)", "Amount ($)"], horizontal=True)

if down_type == "Percentage (%)":
    down_percent = st.number_input("Down Payment (%)", min_value=0.0, max_value=100.0, value=20.0, step=0.1)
    down_payment = home_price * down_percent / 100
else:
    down_payment = st.number_input("Down Payment ($)", min_value=0.0, max_value=home_price, value=60000.0, step=1000.0)

loan_amount = home_price - down_payment

rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, value=3.5, step=0.1)
years = st.number_input("Loan Term (years)", min_value=1, value=30, step=1)

monthly_rate = rate / 100 / 12
n_payments = years * 12

if monthly_rate > 0:
    payment = loan_amount * monthly_rate / (1 - (1 + monthly_rate) ** -n_payments)
else:
    payment = loan_amount / n_payments

col1, col2, col3 = st.columns(3)
col1.metric(label="Down Payment", value=f"${down_payment:,.2f}")
col2.metric(label="Loan Amount", value=f"${loan_amount:,.2f}")
col3.metric(label="Monthly Payment", value=f"${payment:,.2f}")
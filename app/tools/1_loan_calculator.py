import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math

st.title("Loan/Mortgage Calculator")

st.write("### Input Loan Details")
col1, col2 = st.columns(2)
home_price = col1.number_input("Home Price ($)", min_value=0.0, value=300000.0, step=1000.0)
rate = col2.number_input("APR (%)", min_value=0.0, value=4.0, step=0.1)
down_percent = col1.number_input("Down Payment (%)", min_value=0.0, max_value=100.0, value=0.0, step=1.0)
years = col2.number_input("Loan Term (years)", min_value=1, value=30, step=1)

down_payment = home_price * down_percent / 100
loan_amount = home_price - down_payment

monthly_rate = rate / 100 / 12
n_payments = years * 12

if monthly_rate > 0:
    payment = loan_amount * monthly_rate / (1 - (1 + monthly_rate) ** -n_payments)
else:
    payment = loan_amount / n_payments

st.write("\n")
st.write("### Load Summary")

col1, col2, col3 = st.columns(3)
col1.metric(label="Down Payment", value=f"${down_payment:,.2f}")
col2.metric(label="Monthly Payment", value=f"${payment:,.2f}")

col1, col2, col3 = st.columns(3)
col1.metric(label="Loan Amount", value=f"${loan_amount:,.2f}")
col2.metric(label="Total Payment", value=f"${down_payment + payment * n_payments:,.2f}")
col3.metric(label="Total Interest", value=f"${(down_payment + payment * n_payments) - loan_amount:,.2f}")

# Create a data-frame with the payment schedule.
schedule = []
remaining_balance = loan_amount
total_interest = 0.0

for i in range(1, n_payments + 1):
    interest_payment = remaining_balance * monthly_rate
    principal_payment = payment - interest_payment
    remaining_balance -= principal_payment
    total_interest += interest_payment
    year = math.ceil(i / 12)  # Calculate the year into the loan
    schedule.append(
        [
            i,
            payment,
            principal_payment,
            interest_payment,
            remaining_balance,
            total_interest,
            year,
        ]
    )

df = pd.DataFrame(
    schedule,
    columns=["Month", "Payment", "Principal", "Interest", "Remaining Balance", "Interest Paid", "Year"],
)

# Display the data-frame as a chart.
st.write("\n")
st.write("### Payment Schedule")
payments_df = df[["Year", "Remaining Balance", "Interest Paid"]].groupby("Year").min()
st.line_chart(payments_df, color=["#f00", "#00f"])
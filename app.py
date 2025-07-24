import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# --- App Title ---
st.set_page_config(page_title="Expense Tracker", page_icon="💰")
st.title("💼 Expense Tracker with Charts")
st.markdown("Track your daily expenses, analyze your spending, and visualize where your money goes. Simple and effective!")

# --- File Setup ---
FILE_PATH = "expenses.csv"

# --- Input Section ---
st.header("📝 Add New Expense")

col1, col2 = st.columns(2)
with col1:
    date = st.date_input("Date")
    category = st.selectbox("Category", ["Food", "Transport", "Bills", "Shopping", "Entertainment", "Other"])
with col2:
    amount = st.number_input("Amount (₹)", min_value=0.0, step=0.5, format="%.2f")

if st.button("➕ Add Expense"):
    new_data = pd.DataFrame([[date, category, amount]], columns=["Date", "Category", "Amount"])
    if os.path.exists(FILE_PATH):
        new_data.to_csv(FILE_PATH, mode='a', header=False, index=False)
    else:
        new_data.to_csv(FILE_PATH, index=False)
    st.success("✅ Expense added successfully!")

# --- View Section ---
st.header("📋 Expense History")

if os.path.exists(FILE_PATH):
    df = pd.read_csv(FILE_PATH)
    df["Date"] = pd.to_datetime(df["Date"])
    st.dataframe(df.sort_values("Date", ascending=False), use_container_width=True)

    # Total Spent
    total = df["Amount"].sum()
    st.metric("💸 Total Spent", f"₹{total:.2f}")

    # Pie Chart
    st.subheader("📊 Spending by Category")
    category_sum = df.groupby("Category")["Amount"].sum()
    fig1, ax1 = plt.subplots()
    ax1.pie(category_sum, labels=category_sum.index, autopct="%1.1f%%", startangle=90)
    ax1.axis("equal")
    st.pyplot(fig1)

    # Optional: Line chart over time
    st.subheader("📈 Spending Over Time")
    daily_sum = df.groupby("Date")["Amount"].sum().reset_index()
    st.line_chart(daily_sum.set_index("Date"))

else:
    st.info("No expenses added yet. Start by adding one above ☝️")

# --- Footer ---
st.markdown("---")
st.markdown("Made with ❤️ by **JOY**")
















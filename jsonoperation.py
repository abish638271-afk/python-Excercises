import streamlit as st
import json
import os

DATA_FILE = "bank_data.json"

# ---------- Save data ----------
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ---------- Load data ----------
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

# ---------- Create Account ----------
def create_account(data, name, pin, balance):
    if name in data:
        st.warning(f"Account for '{name}' already exists!")
    else:
        data[name] = {"account_holder": name, "pin": pin, "balance": balance}
        save_data(data)
        st.success(f"✅ Account for {name} created successfully!")
    return data

# ---------- Display Accounts ----------
def display_accounts(data):
    if not data:
        st.info("No accounts found.")
    else:
        st.subheader("🏦 All Bank Accounts")
        for acc in data.values():
            st.write(f"**Name:** {acc['account_holder']}")
            st.write(f"**PIN:** {acc['pin']}")
            st.write(f"**Balance:** ₹{acc['balance']}")
            st.markdown("---")

# ---------- Update Account ----------
def update_account(data, name, pin=None, balance=None):
    if name not in data:
        st.warning(f"Account for '{name}' does not exist!")
    else:
        if pin:
            data[name]["pin"] = pin
        if balance is not None:
            data[name]["balance"] = balance
        save_data(data)
        st.success(f"✅ Account for {name} updated successfully!")
    return data

# ---------- Delete Account ----------
def delete_account(data, name):
    if name in data:
        del data[name]
        save_data(data)
        st.success(f"🗑️ Account '{name}' deleted successfully!")
    else:
        st.warning(f"Account for '{name}' does not exist!")
    return data

# ---------- Main Streamlit App ----------
def main():
    st.title("🏦 Bank Account Manager")
    st.sidebar.header("Navigation")

    menu = st.sidebar.radio(
        "Choose an action",
        ["Create Account", "View Accounts", "Update Account", "Delete Account"]
    )

    data = load_data()

    if menu == "Create Account":
        st.subheader("🧾 Create a New Account")
        name = st.text_input("Enter account holder name")
        pin = st.text_input("Enter 4-digit PIN", type="password", max_chars=4)
        balance = st.number_input("Enter initial balance", min_value=0.0, format="%.2f")
        if st.button("Create Account"):
            if name and pin:
                data = create_account(data, name, pin, balance)
            else:
                st.warning("Please fill all fields.")

    elif menu == "View Accounts":
        display_accounts(data)

    elif menu == "Update Account":
        st.subheader("✏️ Update Account Details")
        name = st.text_input("Enter the account holder name to update")
        new_pin = st.text_input("Enter new PIN (optional)", type="password", max_chars=4)
        new_balance = st.number_input("Enter new balance (optional)", min_value=0.0, format="%.2f")

        if st.button("Update Account"):
            if name:
                data = update_account(data, name, new_pin if new_pin else None, new_balance)
            else:
                st.warning("Please enter an account name.")

    elif menu == "Delete Account":
        st.subheader("❌ Delete Account")
        name = st.text_input("Enter the account holder name to delete")
        if st.button("Delete Account"):
            if name:
                data = delete_account(data, name)
            else:
                st.warning("Please enter an account name.")

if __name__ == "__main__":
    main()

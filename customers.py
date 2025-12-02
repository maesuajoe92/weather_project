customers = {
    "Joe": 2000.75,
    "Alice": 3050.50,
    "Bob": 150.00,
    "Diana": 4200.00,
    "Eve": 980.25,
}

# print all customers and their balances
for name, balance in customers.items():
    print(f"{name}: ${balance:.2f}")

# fitler customers with high balances
high_balance_customers = {
    name: balance for name, balance in customers.items() if balance > 500
}
print("\nCustomers with balances over $500:")
for name, balance in high_balance_customers.items():
    print(f"{name}: ${balance:.2f}")

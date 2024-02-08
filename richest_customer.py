#Code to find the customer with max total balance in all banks

def find_richest_customer(customers):
    max_wealth = 0
    richest_customer = None
    for customer in customers:
        wealth = sum(customer)
        if wealth > max_wealth:
            max_wealth = wealth
            richest_customer = customer

    return richest_customer

# Example usage:
customers = [
    [1000, 200, 300],  # Customer 1
    [400, 500, 600],  # Customer 2
    [700, 800, 900]   # Customer 3
]

richest_customer = find_richest_customer(customers)
print("Richest customer:", richest_customer)
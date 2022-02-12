sandwich_orders = ['hotdog', 'pastrami', 'bacon', 'pastrami', 'cheese', 'pastrami', 'beef']

print("\nPastrami sandwiches were sold out.")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

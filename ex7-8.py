sandwich_orders = ['hotdog', 'bacon', 'cheese', 'beef']

finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich.title() + " sandwich")
    finished_sandwiches.append(current_sandwich)

print("\nAll the sandwiches have been finished.\n")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche)

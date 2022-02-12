"""
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
"""


# def make_pizza(*toppings):
#    """Print all ingredients ordered by the customer"""
#    print(toppings)


# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')
# def make_pizza(*toppings):
#    """Describe the pizza to be made briefly"""
#    print("\nMaking a pizza with the following toppings:")
#    for topping in toppings:
#        print(f"- {topping}")


# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# def make_pizza(size, *toppings):
#    """Overview of pizza to be made"""
#    print(f"\nMaking a {size}-inch pizza with the following toppings: ")
#    for topping in toppings:
#        print(f"- {topping}")


# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

def make_pizza(size, *toppings):
    """Overview of the pizza"""
    print(f"\nMake a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")

prompt = "Please input a ingredient: "
prompt += "\n(Enter 'quit' when you are finished)"
while True:
    ingredients = input(prompt)
    if ingredients == 'quit':
        break
    else:
        print(f"We will add this {ingredients}.")

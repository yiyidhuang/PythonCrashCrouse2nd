def print_model(unprinted_designs, completed_models):
    """Using while loop to find the unprinted list"""
    while unprinted_designs:
        # take out the element from the bottom of unprinted_list and move it into the current_design
        current_design = unprinted_designs.pop()
        # display the value model
        print("Printing " + current_design)
        completed_models.append(current_design)


def x_models(completed_models):
    print("Display the model: ")
    for x_model in completed_models:
        print(x_model)

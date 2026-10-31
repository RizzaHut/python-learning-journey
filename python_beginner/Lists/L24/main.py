def check_ingredient_match(recipe, inventory):
    missing_ingredients = []

    for item in recipe:
        if item not in inventory:
            missing_ingredients.append(item)

    percentage = ((len(recipe) - len(missing_ingredients)) / len(recipe) ) * 100.0

    return percentage, missing_ingredients


import json

# Function to load existing recipes from a file
def load_recipes():
    try:
        with open("recipes.json", "r") as file:
            recipes = json.load(file)
    except FileNotFoundError:
        recipes = []
    return recipes

# Function to save recipes to a file
def save_recipes(recipes):
    with open("recipes.json", "w") as file:
        json.dump(recipes, file, indent=2)

# Function to display all recipes with details
def display_all_recipes(recipes):
    print("\nRecipes:")
    for index, recipe in enumerate(recipes, start=1):
        print(f"\n{index}. {recipe['name']}")
        print("Ingredients:", ", ".join(recipe['ingredients']))
        print("Instructions:")
        print(recipe['instructions'])

# Function to add a new recipe
def add_recipe():
    name = input("Enter recipe name: ")
    ingredients = input("Enter ingredients (comma-separated): ").split(",")
    instructions = input("Enter instructions (comma-separated):  ")

    recipe = {
        "name": name,
        "ingredients": [ingredient.strip() for ingredient in ingredients],
        "instructions": instructions
    }

    return recipe

# Main function
def main():
    recipes = load_recipes()

    while True:
        print("\nRecipe App Menu:")
        print("1. Display Recipes")
        print("2. Add Recipe")
        print("3. Exit")

        user_input = input("Enter your choice (1/2/3): ")

        if user_input == "1":
            display_all_recipes(recipes)
        elif user_input == "2":
            new_recipe = add_recipe()
            recipes.append(new_recipe)
            save_recipes(recipes)
            print("Recipe added successfully!")
        elif user_input == "3":
            print("Exiting Recipe App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

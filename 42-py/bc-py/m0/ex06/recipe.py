from typing import TypedDict
import sys

RecipeName = str

# allows multiple values per key
Recipe = TypedDict("Recipe", {"ingredients": list[str], "meal": str, "prep_time": int})

cookbook: dict[RecipeName, Recipe] = {
    "sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10,
    },
    "cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60,
    },
    "salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15,
    },
}


# lists all recipe names
def list_recipe_names() -> None:
    for name in cookbook:
        print("- " + name)


# prints a recipe with its details
def print_recipe(name: RecipeName) -> None:
    print("Ingriedients list for " + name + ":")
    for ingredient in cookbook[name]["ingredients"]:
        print("- " + ingredient)
    print(f"Meal type: {cookbook[name]['meal']}")
    print(f"Preparation time: {cookbook[name]['prep_time']} min")


# deletes a recipe
def delete_recipe(name: RecipeName) -> None:
    del cookbook[name]
    print(f"{name} was deleted")


# creates a new recipe with user input
def add_recipe() -> None:
    name: str = input("Name of the new recipe: ")
    ingredients: list[str] = input("Ingredients (comma separated): ").split(", ")
    meal: str = input("Type of meal: ")
    prep_time: int = int(input("Preparation time in minutes: "))
    cookbook[name] = {"ingredients": ingredients, "meal": meal, "prep_time": prep_time}
    print(f"{name} was added")


# prints the list of available options
def list_options() -> None:
    print("List of available option:")
    print("  1: Add a recipe")
    print("  2: Delete a recipe")
    print("  3: Print a recipe")
    print("  4: Print the cookbook")
    print("  5: Quit")


if __name__ == "__main__":
    print("Welcome to the Python Cookbook !")
    list_options()
    while True:
        print("\nPlease select an option: ")

        option: str = input(">> ")
        if option == "1":
            add_recipe()
        elif option == "2":
            name: str = input("Name of the recipe to delete: ")
            delete_recipe(name)
        elif option == "3":
            name: str = input("Name of the recipe: ")
            print_recipe(name)
        elif option == "4":
            list_recipe_names()
        elif option == "5":
            print("Cookbook closed. Goodbye !")
            sys.exit()
        else:
            print("Invalid option, please retry !")
            list_options()

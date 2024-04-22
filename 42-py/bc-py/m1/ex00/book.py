from typing import Literal, get_args

import datetime
from recipe import Recipe

MealCategories = Literal["starter", "lunch", "dessert"]
MEAL_CATEGORIES : list[MealCategories] = list(get_args(MealCategories))

class Book:
    def __init__(self,
        name          : str,
        last_update   : datetime.datetime,
        creation_date : datetime.datetime,
        recipes_list  : dict[MealCategories, list[Recipe]],
    ) -> None:
        if not name:
            raise ValueError("name must not be empty")
        self.name = name

        self.last_update = last_update

        self.creation_date = creation_date

        if (
            not all([key in recipes_list.keys() for key in MEAL_CATEGORIES     ]) or
            not all([key in MEAL_CATEGORIES     for key in recipes_list.keys() ])
        ):
            raise ValueError("recipes_list must contain 'starter', 'lunch' and 'dessert'")
        self.recipes_list = recipes_list

    def get_recipe_by_name(self, name :str) -> Recipe:
        """Prints a recipe with the name `name` and returns the instance"""
        for recipe in self.recipes_list.values():
            for r in recipe:
                if r.name == name:
                    return r
        raise ValueError(f"Recipe with name '{name}' not found")

    def get_recipes_by_types(self, recipe_type :str) -> list[Recipe]:
        """Get all recipe names for a given recipe_type"""
        if not recipe_type in MEAL_CATEGORIES:
            raise ValueError(f"{recipe_type} is not a valid recipe type")
        return self.recipes_list[recipe_type]

    def add_recipe(self, recipe :Recipe) -> None:
        """Add a recipe to the book and update last_update"""
        if not recipe.recipe_type in MEAL_CATEGORIES:
            raise ValueError(f"{recipe.recipe_type} is not a valid recipe type")
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.datetime.now()

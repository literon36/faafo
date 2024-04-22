class Recipe:
    def __init__(self,
        name         : str,
        cooking_lvl  : int,
        cooking_time : int,
        ingredients  : list[str],
        recipe_type  : str,
    ) -> None:
        if not name:
            raise ValueError("name must not be empty")
        self.name = name

        if not cooking_lvl in range(1, 5):
            raise ValueError("cooking_lvl must be between 1 and 5")
        self.cooking_lvl = cooking_lvl

        if not cooking_time > 0:
            raise ValueError("cooking_time must be greater than 0")
        self.cooking_time = cooking_time

        if not ingredients:
            raise ValueError("ingredients must not be empty")
        self.ingredients = ingredients

        if not recipe_type in ["starter", "lunch", "dessert"]:
            raise ValueError("recipe_type must be 'starter', 'lunch' or 'dessert'")
        self.recipe_type = recipe_type

    def __str__(self) -> str:
        txt : str = ""
        txt += f"Recipe name: {self.name}\n"
        txt += f"Difficulty: {self.cooking_lvl}\n"
        txt += f"Expected cooking time: {self.cooking_time} min\n"
        txt += f"Ingredients: {', '.join(self.ingredients)}\n"
        txt += f"Recipe type: {self.recipe_type}\n"
        return txt
    
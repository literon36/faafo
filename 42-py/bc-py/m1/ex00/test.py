from book import Book
from recipe import Recipe
import datetime
import unittest

from typing import Literal
MealCategories = Literal["starter", "lunch", "dessert"]

# test creation of a recipe with bad values
class TestRecipeCreation(unittest.TestCase):
    """Test the creation of a recipe with bad values"""

    def test_bad_name(self):
        """Test that an error is raised when name is empty"""
        with self.assertRaises(ValueError):
            Recipe("", 2, 30, ["onion", "cheese"], "starter")

    def test_bad_cooking_level(self):
        """Test that an error is raised when cooking_lvl is not between 1 and 5"""
        with self.assertRaises(ValueError):
            Recipe("test", 0, 30, ["onion", "cheese"], "starter")
        with self.assertRaises(ValueError):
            Recipe("test", 6, 30, ["onion", "cheese"], "starter")

    def test_bad_cooking_time(self):
        """Test that an error is raised when cooking_time is not greater than 0"""
        with self.assertRaises(ValueError):
            Recipe("test", 2, 0, ["onion", "cheese"], "starter")

    def test_bad_ingredients_empty(self):
        """Test that an error is raised when ingredients is empty"""
        with self.assertRaises(ValueError):
            Recipe("test", 2, 30, [], "starter")

    def test_bad_recipe_type(self):
        """Test that an error is raised when recipe_type is not 'starter', 'lunch' or 'dessert'"""
        with self.assertRaises(ValueError):
            Recipe("test", 2, 30, ["onion", "cheese"], "spaghetti")

# test __str__ of a recipe
class TestRecipeStr(unittest.TestCase):
    """Test the __str__ of a recipe"""

    def test_str(self):
        """Test the __str__ of a recipe"""
        recipe = Recipe("test", 2, 30, ["onion", "cheese"], "starter")
        self.assertEqual(str(recipe), "Recipe name: test\nDifficulty: 2\nExpected cooking time: 30 min\nIngredients: onion, cheese\nRecipe type: starter\n")


# test creation of a book with bad values
class TestBookInit(unittest.TestCase):
    """Test the creation of a book with bad values"""
    
    recipes : dict[MealCategories, list[Recipe]] = {
        "starter": [Recipe("test", 2, 30, ["onion", "cheese"], "starter")],
        "lunch": [Recipe("test", 2, 30, ["onion", "cheese"], "lunch")],
        "dessert": []
    }

    def test_bad_name(self):
        """Test that an error is raised when name is empty"""
        with self.assertRaises(ValueError):
            Book("", datetime.datetime.now(), datetime.datetime.now(), self.recipes)

    def test_bad_recipes_list(self):
        """Test that an error is raised when recipes_list does not contain 'starter', 'lunch' and 'dessert'"""
        with self.assertRaises(ValueError):
            Book(
                "test",
                datetime.datetime.now(),
                datetime.datetime.now(),
                {
                    "starter": [Recipe("test", 2, 30, ["onion", "cheese"], "starter")]
                }
            )   

# test book functions
class TestBookFunctions(unittest.TestCase):
    """Test the book functions"""

    def test_get_recipe_by_name(self):
        """Test the get_recipe_by_name function"""
        book = Book(
            "test",
            datetime.datetime.now(),
            datetime.datetime.now(),
            {
                "starter": [Recipe("test", 2, 30, ["onion", "cheese"], "starter")],
                "lunch": [Recipe("not_test", 2, 30, ["onion", "cheese"], "lunch")],
                "dessert": []
            }
        )
        test_recipe = book.get_recipe_by_name("test")
        self.assertEqual(test_recipe.name, "test")


    def test_get_recipes_by_types(self):
        """Test the get_recipes_by_types function"""
        book = Book(
            "test",
            datetime.datetime.now(),
            datetime.datetime.now(),
            {
                "starter": [Recipe("test", 2, 30, ["onion", "cheese"], "starter"),
                            Recipe("test2", 2, 30, ["onion", "cheese"], "starter")],
                "lunch": [],
                "dessert": []
            }
        )
        #print(book.get_recipes_by_types("starter"))
        recipe :list[Recipe]= book.get_recipes_by_types("starter")
        self.assertEqual(len(recipe), 2)
        self.assertEqual(recipe[0].name, "test")
        self.assertEqual(recipe[1].name, "test2")



if __name__ == "__main__":
    unittest.main()
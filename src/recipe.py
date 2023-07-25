"""Natalie Ferraro recipe.py

recipe.py module is a class for defining recipes.
"""

class Recipe:
    """Recipe class defines a recipe object."""
    
    def __init__(self, recipe_name, ingredients, directions, nutrition):
        """__init__ constructor method.
        
        Info that defines a recipe object: recipe name, ingredients, directions, and nutrition.
        """
        self.recipe_name = recipe_name
        self.ingredients = ingredients
        self.directions = directions       
        self.nutrition = nutrition
    
    def return_name(self):
        """return_name method returns the name of the recipe."""
        return self.recipe_name
    
    def return_ingredients(self):
        """return_ingredients method returns the ingredients of a recipe."""
        return self.ingredients
    
    def return_directions(self):
        """return_directions method returns the directions neccessary for cooking a recipe."""
        return self.directions
    
    def return_nutrition(self):
        """return_nutrition method returns the nutrition info of a recipe."""
        return self.nutrition
    
    def print_recipe(self):
        """print_recipe method prints the name of the recipe, ingredients, directions, and nutrition info."""
        print(self.recipe_name)
        print("Ingredients:", self.ingredients)
        print("Directions:", self.directions)
        print("Nutrition Info:", self.nutrition)
          
if __name__ == "__main__":
    #the code inside the if statement is not executed when the file's code is imported as a module.
    recipe = Recipe(
        "PBJ", 
        "Peanut butter, jelly, bread",
        "Spread the peanut butter on one slice of bread. Spread the jelly on the other piece of bread. Put the two pieces of bread together.",
        "Nutritious and delicious."
    )
    recipe.print_recipe()
    
"""
Natalie Ferraro recipe.py
recipe.py module is the foundational class for storing recipes in the cookbook app.
"""

class Recipe:
    """Recipe class defines the four components of a recipe.
    
    Args:
        None.
        
    Returns:
        None.
    """
    
    def __init__(self):
        """__init__ constructor method recieves input from the user about recipe name, ingredients, directions, and nutrition when an object of the Recipe class is created.
        
        Args:
            None.
            
        Returns:
            None.        
        """
        
        self.recipe_name = input("Enter the name of the recipe: ")
        #recipe name string
        
        self.ingredients = input("Enter the ingredients: ")
        #ingredients string
        
        self.directions = input("Enter the directions (in the correct order): ")            
        #directions string
        
        self.nutrition = input("Enter the nutrion info pertaining to this recipe (calories, etc): ")
        #get nutrition info.
            
    def return_name(self):
        """return_name method returns the name of the recipe.
        
        Args:
            None.
            
        Returns:
            recipe_name.        
        """
        
        return self.recipe_name
    
    def return_ingredients(self):
        """return_ingredients method returns the ingredients of a recipe.
        
        Args:
            None.
            
        Returns:
            ingredients.      
        """
        
        return self.ingredients
    
    def return_directions(self):
        """return_directions method returns the directions neccessary for cooking a recipe.
        
        Args:
            None.
            
        Returns: 
            directions.        
        """
        
        return self.directions
    
    def return_nutrition(self):
        """return_nutrition method returns the nutrition info of a recipe
        
        Args:
            None.
            
        Returns:
            nutrition.        
        """
        
        return self.nutrition
    
    def print_recipe(self):
        """print_recipe method prints the name of the recipe, ingredients, directions, and nutrition info.
        
        Args:
            None.
            
        Returns:
            None.
        """
        
        print("\n", self.recipe_name)
        print("Ingredients:\n", self.ingredients)
        print("Directions:\n", self.directions)
        print("Nutrition Info:\n", self.nutrition)
          
if __name__ == "__main__":
    #the code inside the if statement is not executed when the file's code is imported as a module.
    recipe = Recipe()
    recipe.print_recipe()
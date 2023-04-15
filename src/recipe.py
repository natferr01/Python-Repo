"""
Natalie Ferraro recipe.py
recipe.py module is the a class for defining recipes.
"""

class Recipe:
    """Recipe class defines the four components of a recipe.
    
    Args:
        None.
        
    Returns:
        None.
    """
    
    def __init__(self, recipe_name, ingredients, directions, nutrition):
        """__init__ constructor method recieves input from the user about recipe name, ingredients, directions, and nutrition when an object of the Recipe class is created.
        
        Args:
            None.
            
        Returns:
            None.        
        """
        
        self.recipe_name = recipe_name
        #recipe name string
        
        self.ingredients = ingredients
        #ingredients string
        
        self.directions = directions       
        #directions string
        
        self.nutrition = nutrition
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
        
        print(self.recipe_name)
        print("Ingredients:", self.ingredients)
        print("Directions:", self.directions)
        print("Nutrition Info:", self.nutrition)
          
if __name__ == "__main__":
    #the code inside the if statement is not executed when the file's code is imported as a module.
    recipe = Recipe("PBJ", 
                    "Peanut butter, jelly, bread",
                    "Spread the peanut butter on one slice of bread. Spread the jelly on the other piece of bread. Put the two pieces of bread together.",
                    "Nutritious and delicious.")
    recipe.print_recipe()
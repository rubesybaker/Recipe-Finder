def add_recipe(recipes, recipe_name, recipe_link, recipe_ingredients, 
recipe_instructions):
  recipes[recipe_name] = {'recipe_ingredients': recipe_ingredients, 'recipe_link': 
                          recipe_link,
                          'recipe_instructions': recipe_instructions}
  
def search_recipes(recipes,search_ingredients):
  matching_recipes = []
  for recipe_name, recipe_data in recipes.items():
    if all(recipe_ingredients.lower() in recipe_data['recipe_ingredients'].lower() for 
           recipe_ingredients in search_ingredients):

      matching_recipes.append(recipe_name)
  return matching_recipes

def display_recipe(recipe_name, recipe_data):
  print(f"Recipe: {recipe_name}")
  print(f"Ingredients: {recipe_data['recipe_ingredients']}")
  print(f"Instructions: {recipe_data['recipe_instructions']}")
  print(f"Link: {recipe_data['recipe_link']}")
  print()
recipes = {}

add_recipe(recipes, "Chocolate_Cake","https://www.recipetineats.com/my-very-best-vanillacake/", 
           "flour, sugar, cocoa powder, eggs, oil, salt, baking powder, milk", 
           "1. sift dry ingredients in a bowl. 2. mix wet ingredients. 3. Gently combine all ingredients. 4. Pour into oiled baking pan. 5. Bake at 350F for 50 min or until \ninserted toothpick comes out clean.")

add_recipe(recipes, "Vanilla_Cake",
   "https://addapinch.com/the-best-chocolate-cake-recipe-ever/",
   "flour, sugar, eggs, butter, salt, baking powder, milk", 
"1. sift dry ingredients in a bowl.\n2. mix wet ingredients.\n3. Gently, fold the wet ingredients in the dry ingredients. 4. pour into oiled baking pan. 5. Bake at 350F for 30 min or until inserted toothpick comes out clean.")

search_ingredients = input("Enter ingredients (comma-separated):").lower().split(',') 

matching_recipes = search_recipes(recipes,search_ingredients)

if matching_recipes:
  print("\nMatching recipes:")
  for i, recipe_name in enumerate(matching_recipes, start=1):
    print(f"{i}. {recipe_name}")  
    choice=input("Enter the number of the recipe you want to view: ")
    if choice.isdigit() and 1 <= int(choice) <= len(matching_recipes): selected_recipe = matching_recipes[int(choice) -1]
    display_recipe(selected_recipe, recipes[selected_recipe])
  
else: 
  print("\nNo matching recipes found.")
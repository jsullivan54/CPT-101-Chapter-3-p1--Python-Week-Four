#Name: Johnathan Sullivan's Family Pancake Recipie
#Program Name: This program contains our family pancake recipie
#Prgram_Description: This program contains our family pancake recipie. /
#The recipie yields 8 pancakes per batch. This program allows the end user to input/
#a specific amount of pancakes and the output will be the ingredient list with respective measurements.


BASE_PANCAKES = 8 #Number of Pancakes the starting recipie creates
BASE_FLOUR = 2 #Number of Cups of flour for base recipie
BASE_SUGAR = 2 #Number of Tablespoons for base recipie
BASE_BAKING_POWDER = 2 #Number of Teaspoons for base recipie
BASE_MILK = 1.5 #Number of  Cups for base recipie
BASE_EGGS = 2 #Number of Large eggs for base recipie
BASE_MELTED_BUTTER = 2 #Number of Tablespoons form base recipie

num_cakes = int(input('Please enter the number of desired pancakes: '))
Multiplier= num_cakes / BASE_PANCAKES
#print (f'Multiplier: is {Multiplier}')
needed_flour = BASE_FLOUR * Multiplier
print(f'Needed flour: {needed_flour:.1f} cups.')
needed_sugar = BASE_SUGAR * Multiplier
print(f'Needed sugar: {needed_sugar:.1f} tablespoons.')
needed_baking_powder = BASE_BAKING_POWDER * Multiplier
print(f'Needed baking powder: {needed_baking_powder:.1f} teaspoons.')
needed_milk = BASE_MILK * Multiplier
print(f'Needed milk: {needed_milk: .1f} cups.')
needed_eggs = BASE_EGGS * Multiplier
print(f'Needed eggs: {needed_eggs:.1f} Large eggs.')
needed_melted_butter = BASE_MELTED_BUTTER * Multiplier
print(f'Needed melted butter : {needed_melted_butter:.1f} tablespoons.')





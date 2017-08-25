pastry = dict = {"plain flour":"300 g","lard":"100 g","salt":"1 tbsp","egg":"1 for egg wash"}
filling = dict = {"small white onion":"1","small green pepper":"1","cloves of garlic":"2","olive oil":"1 tbsp","minced beef":"250 g","paprika":"1/2 tsp","ground cumin":"1/2 tps","chili powder":"1/2 tsp","salt":"1 tsp","ground black pepper":"1/2 tsp","tomato puree":"1 tbsp"}
more_filling = dict = {"eggs":"2","green pimento stuffed olives":"1 handful"}
filling.update(more_filling)
chimichurri = dict = {"handful of fresh corainder":"1","cloves of garlic":"2","red wine vinegar":"1 tbsp","dried oregano":"1/2 tsp","dried chili flakes":"1/2 tsp","lime":"1","olive oil":"2 tbsp"}

instructions = ["PASTRY: Add the flour, salt and lard into a food processor and blitz into breadcrumbs. Pour in approximately 50-70ml of water gradually, mixing until a dough is just formed. Wrap the dough in clingfilm and rest in the fridge for an hour.","BEEF FILLING START: Chop the onion finely, and do the same for the garlic and green pepper, then fry in a pan with olive oil until softened. Add the minced beef and fry over a high heat until browned. Stir in the spices and tomato purée. Remove from the heat and leave to cool to room temperature.","BEEF FILLING FINISH: Boil the eggs in salted boiling water for 8-9 minutes then run under cold water for as many minutes again. Peel the eggs and roughly chop. Drain the olives and roughly chop those too. Stir in the olives and chopped eggs."]

instructions.extend(["ROLL, FILL, FOLD, CRIMP: Preheat the oven to 180°C. Roll out the pastry on a floured surface to the thickness of a pound coin. Cut out circles from the pastry, using a saucer or bowl as a guide. Spoon two teaspoons of the filling onto one half of each pastry circle. Brush the edge with egg, fold over and crimp the edges together at the side.","BAKE: Brush with egg, place on a baking try and bake for 30 minutes until golden.","CHIMICHURRI SAUCE: Add all ingredients for the chimichurri into a food processor and blitz till smooth."])

print("Spicy Beef Empanadas")
print("SortedFood.com")
print("   ")
print("Pastry Ingredients:")
print(pastry)
print("   ")
print("Filling Ingredients:")
print(filling)
print("   ")
print("chimichurri Ingredients")
print(chimichurri)
print("   ")
print("Instructions")
for i in instructions:
    print (i)

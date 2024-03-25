items = ( ('beans' , 'fanta' , 'dare'), ('rice' , 'coke' , 'aremu',), ('spag' , 'viju' , 'bolu',) )
food ,drink,name = items
foods =[]
for food, _,_ in items:
    foods.append(food)
print(foods)
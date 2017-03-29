pizzas = ['pepperoni', 'hawaiian', 'cheese', 'seafood', 'meat', 'vegetable']
for pizza in pizzas:
	print('I like ' + pizza + ' pizza')
print('I really love pizza!')
print('The first three items in the list are:')
for pizza in pizzas[:3]:
	print(pizza)
print('The items from the middle of the list are:')
for pizza in pizzas[2:5]:
	print(pizza)
print('The last three items in the list are:')
for pizza in pizzas[-3:]:
	print(pizza)

friend_pizzas = pizzas[:]
pizzas.append('beaf')
friend_pizzas.append('korean pickles')
print('\nMy favorite pizzas are:')
for pizza in pizzas:
	print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)

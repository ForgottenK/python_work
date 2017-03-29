sandwich_orders = ['Ham and egg sandwich', 'Salad sandwich', 'Salmon sandwich'
	, 'Pastrami sandwich', 'Tuna sandwich', 'Pastrami sandwich', 'Pastrami sandwich']
finished_sandwiches = []
print('The pastrami is sold out, so that we can not make pastrami sandwich.')
while 'Pastrami sandwich' in sandwich_orders:
	sandwich_orders.remove('Pastrami sandwich')
while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print('I made your ' + sandwich)
	finished_sandwiches.append(sandwich)
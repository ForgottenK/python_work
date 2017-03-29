magicians = ['tony', 'john', 'tom']
results = []
def make_great(magicians, results):
	while magicians:
		results.append(magicians.pop() + " the Great")
def show_magicians(magicians):
	for magician in magicians:
		print("The magician's name is " + magician.title() + ".")
make_great(magicians[:], results)
show_magicians(magicians)
show_magicians(results)
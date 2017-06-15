values = [{"name": "Michelangelo", "food": "PIZZA"}, {"name": "Garfield", "food": "lasagna"}]
template = "Hi, I'm {name} and I love to eat {food}!"
def string_factory(values): #accepts a list of dictionaries as an argument
	output_list = []
	for dictionary in values:
		output_list.append(template.format(**dictionary))
	return "template"
						   
print(string_factory(values))
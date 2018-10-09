"""Restaurant rating lister."""
import sys

file_name = sys.argv[1]

restaurant_dict = {}

with open(file_name) as file:

	for line in file:
		line = line.strip()
		word = line.split(':')
		#print(word)
		restaurant_dict[word[0]] = word[1]

		#restaurant, score = line.strip().split(':')
		#restaurant_dict[restaurant] = score


		
# i = sorted(restaurant_dict)

# print(restaurant_dict)


#1st approach

def restaurants_display():
	for restaurant in sorted(restaurant_dict.items()):
		print('{}: {}'.format(restaurant[0], restaurant[1]))


restaurants_display()



#2nd approach
# boo = [print('{}: {}'.format(restaurant[0], restaurant[1])) for restaurant in restaurant_dict.items()]


#3rd approach
# boo = ['{}: {}'.format(restaurant[0], restaurant[1]) for restaurant in restaurant_dict.items()]
# for i in sorted(boo):
# 	print(i)

new_restaurant = input("Please provide Restaurant name: ").title()
raiting = input("Please rate the restaurant: ")


restaurant_dict[new_restaurant] = raiting

# for restaurant in sorted(restaurant_dict.items()):
# 	print('{}: {}'.format(restaurant[0], restaurant[1]))

restaurants_display()







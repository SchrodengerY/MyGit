'''This is "nester.py" module, which provides a func named print_lol().
we can use this func to print list, which may include(or not) cycle list.
'''


def print_lol(the_list):
	'''This function takes one positional argument called "the_list", which is any Python list.
	:param the_list: It is a list.
	:return: Each item in the list.
	'''
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item)
		else:
			print(each_item)
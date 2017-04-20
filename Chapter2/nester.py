'''This is "nester.py" module, which provides a func named print_lol().
we can use this func to print list, which may include(or not) cycle list.
'''


def print_lol(the_list, indent = False, level = 0):
	'''This function takes one positional argument called "the_list", which is any Python list.
	:param the_list: It is a list.
	:return: Each item in the list.
	'''
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item, level+1)
		else:
			if indent:
				for tab_stop in range(level):
					print('\t', end='')
			print(each_item)
#main-code
man = []
other = []

try:
	data = open('sketch.txt')
	for each_line in data:
		try:
			(role, line_spoken) = each_line.split(':',1)
			line_spoken = line_spoken.strip()
			if role == 'Man':
				man.append(line_spoken)
			elif role == 'Other Man':
				other.append(line_spoken)
		except ValueError:
			pass
	data.close()
except IOError:
	print('The datafile is missing.')

#code-version 1.0
try:
	out_man = open('man_data.txt', 'w+')
	out_other = open('other_data.txt', 'w+')
	print(man, file = out_man)
	print(other, file = out_other)

	out_man.close()
	out_other.close()

except IOError:
	print('File Error.')

#code-version 2.0
try:
	out_man = open('man_data.txt', 'w+')
	out_other = open('other_data.txt', 'w+')
	print(man, file = out_man)
	print(other, file = out_other)

except IOError:
	print('File Error.')

finally:
	out_man.close()
	out_other.close()

#code-version 3.0
try:
	with open('man_data.txt', 'w') as man_file:
		print(man, file = man_file)
	with open('other_data.txt', 'w') as other_file:
		print(other, file = other_file)
except IOError as err:
	print('File Error: ' + str(err))
#code-version 3.1
try:
	with open('man_data.txt', 'w') as man_file, open('other_data.txt', 'w') as other_file:
		print(man, file = man_file)
		print(other, file = other_file)
except IOError as err:
	print('File Error: ' + str(err))

#code-version 4.0
import sys
def print_lol(the_list, indent = False, level = 0, position = sys.stdout):

	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item, indent, level+1, position)
		else:
			if indent:
				for tab_stop in range(level):
					print('\t', end='', file = position)
			print(each_item, file = position)

try:
	with open('man_data.txt', 'w') as man_file, open('other_data.txt', 'w') as other_file:
		print_lol(man, False, 0, man_file)
		print_lol(other, False, 0, other_file)
except IOError as err:
	print('File Error:' + str(err))

#code-version 5.0
import sys
import pickle

try:
	with open('man_data.txt', 'wb') as man_file, open('other_data.txt', 'wb') as other_file:
		pickle.dump(man, man_file); pickle.dump(other,other_file)
except IOError as err:
	print('File error: ' + str(err))
except pickle.PickleError as perr:
	print('Pickle error:' + str(perr))



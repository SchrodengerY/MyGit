'''the_file = open('sketch.txt')

# Do something with the data
# in "the_file"

the_file.close()'''

import os
#print(os.getcwd())
#os.chdir('../HeadFirst1/Chapter3')
#print(os.getcwd())

data = open('sketch.txt')
print(data.readline(), end='')
#print('\n')
data.seek(0)
for each_line in data:
	if each_line.find(':') != -1:
		(role, line_spoken) = each_line.split(':', 1)
		print(role, end='')
		print('said: ', end='')
		print(line_spoken, end='')
	else:
		print(each_line, end='')
	#print(each_line, end='')
data.close()


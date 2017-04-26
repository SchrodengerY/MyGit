james = []
julie = []
mikey = []
sarah = []

with open('james.txt') as jaf:
	data = jaf.readline()
james = data.strip().split(',')   #

with open('julie.txt') as juf:
	data = juf.readline()
julie = data.strip().split(',')

with open('mikey.txt') as mif:
	data = mif.readline()
mikey = data.strip().split(',')

with open('sarah.txt') as saf:
	data = saf.readline()
sarah = data.strip().split(',')

def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return (time_string)
	(mins, secs) = time_string.split(splitter)
	return (mins + '.' + secs)

james = sorted([sanitize(t) for t in james])
julie = sorted([sanitize(t) for t in julie])
mikey = sorted([sanitize(t) for t in mikey])
sarah = sorted([sanitize(t) for t in sarah])

# data processing version 1.0
unique_james = []
unique_julie = []
unique_mikey = []
unique_sarah = []
for each_t in james:
	if each_t not in unique_james:
		unique_james.append(each_t)
		if len(unique_james) == 3:
			break

print(unique_james)

#data processing version 2.0: 用集合(set)删除重复项
print('\n')
with open('james.txt') as jaf:
	data = jaf.readline()
james = data.strip().split(',')   #

with open('julie.txt') as juf:
	data = juf.readline()
julie = data.strip().split(',')

with open('mikey.txt') as mif:
	data = mif.readline()
mikey = data.strip().split(',')

with open('sarah.txt') as saf:
	data = saf.readline()
sarah = data.strip().split(',')

def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return (time_string)
	(mins, secs) = time_string.split(splitter)
	return (mins + '.' + secs)

print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])


#将with写成函数形式 version 3.0:
def proc(file):
	try:
		with open(file) as f:
			data = f.readline()
		return (data.strip().split('.'))
	except IOError as ioerr:
		print('File error:' + str(ioerr))
		return (None)

james = proc('james.txt')
julie = proc('julie.txt')
mikey = proc('mikey.txt')
sarah = proc('sarah.txt')
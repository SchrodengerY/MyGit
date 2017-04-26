#data processing

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

print(james)
print(julie)
print(mikey)
print(sarah)

#data sorting
print('\nSorted Data')
print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))

# sort:替换排序； sorted:复制排序

def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return (time_string)
	(mins, secs) = time_string.split(splitter)
	return (mins + '.' + secs)

james1 = []
julie1 = []
mikey1 = []
sarah1 = []

for t in james:
	james1.append(sanitize(t))
for t in julie:
	julie1.append(sanitize(t))
for t in mikey:
	mikey1.append(sanitize(t))
for t in sarah:
	sarah1.append(sanitize(t))

print('\n修改后的排序')
print(sorted(james1))
print(sorted(julie1))
print(sorted(mikey1))
print(sorted(sarah1))

# 需要降序排列时，传入参数reverse = True

# list comprehension
clean_mikey = [sanitize(each_t) for each_t in mikey]
lower = ['I', "don't", "like", "spam"]
upper = [s.upper() for s in lower]
print(upper)

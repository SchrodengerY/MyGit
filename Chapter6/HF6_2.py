#继承类
#demo:
class NamedList(list):
	def __init__(self, a_name):
		list.__init__([])
		self.name = a_name


#AthleteList:
def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return time_string
	(mins, secs) = time_string.split(splitter)
	return(mins + '.' + secs)

class AthleteList(list):
	def __init__(self, a_name, a_dob = None, a_times = []):
		list.__init__([])
		self.name  = a_name
		self.dob   = a_dob
		self.extend(a_times)

	def top3(self):
		return(sorted(set([sanitize(t) for t in self]))[0:3])   #时间数据自身是self

def get_coach_data(filename):
	try:
		with open(filename) as f:
			data = f.readline()
		templ = data.strip().split(',')
		return(AthleteList(templ.pop(0), templ.pop(0), templ))
	except IOError as ioerr:
		print('File error:' + str(ioerr))
		return(None)

vera = AthleteList('vera vici')
vera.append('1.31')
print(str(vera.top3()))
vera.extend(['1:22', '3-21', '5.04'])
print(str(vera.top3()))


# 写在最后的说明：可以将类放在模块文件中，使用方法为
#              1. 首先将AthleteList类保存到一个名为atheltelist.py的文件中
#              2. from athletelist import AthleteList
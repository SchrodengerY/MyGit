#定制数据对象
def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return time_string
	(mins, secs) = time_string.split(splitter)
	return(mins + '.' + secs)

def get_coach_data(filename):
	try:
		with open(filename) as f:
			data = f.readline()
		return(data.strip().split(','))
	except IOError as ioerr:
		print('File error:' + str(ioerr))
		return(None)

sarah = get_coach_data('sarah2.txt')
(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
print(sarah_name + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in sarah]))[0:3]))

#version 1.1: 使用字典(关联数组)
sarah = get_coach_data('sarah2.txt')
athleter_sarah = dict()
athleter_sarah['name'] = sarah.pop(0)
athleter_sarah['dob'] = sarah.pop(0)
athleter_sarah['time'] = sarah
print(athleter_sarah['name'] + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in athleter_sarah['time']]))[0:3]))

#version 1.2: 新版本的get_coacah_data()
def get_coach_data_new(filename):
	try:
		with open(filename) as f:
			data = f.readline()
		data = data.strip().split(',')
		athleter = dict()
		athleter['name'] = data.pop(0)
		athleter['dob'] = data.pop(0)
		athleter['time'] = data
		athleter['time'] = str(sorted(set([sanitize(t) for t in athleter['time']]))[0:3])
		return athleter
	except IOError as ioerr:
		print('File error: ' + str(ioerr))
		return None

sarah_data = get_coach_data_new('sarah2.txt')
print(sarah_data['name'] + "'s fastest times are: " + sarah_data['time'])

#version 2.0: 使用类
class Athlete:
	def __init__(self, a_name, a_dob = None, a_times = []):
		#This code is used for 用来定义对象的初始状态
		self.name = a_name
		self.dob = a_dob
		self.times = a_times

	def top3(self):
		return sorted(set([sanitize(t) for t in self.times]))[0:3]

	def add_time(self, a_t):
		self.times.append(a_t)

	def add_times(self, a_ts):
		self.times.extend(a_ts)

def get_coach_data_class(filename):
	try:
		with open(filename) as f:
			data = f.readline()
		templ = data.strip().split(',')
		a = Athlete(templ.pop(0), templ.pop(0), templ)
		return a
	except IOError as ioerr:
		print('File error: ' + str(ioerr))
		return None

sarah_class = get_coach_data_class('sarah2.txt')
print(sarah_class.name + "'s fastest times are: " + str(sarah_class.top3()))

# 测试add_time 和 add_times的功能
vera = Athlete('vera vi')
vera.add_time('1.32')
print(str(vera.top3()))
vera.add_times(['2.22', '1-21', '2:22'])
print(str(vera.top3()))
# 1.LIST 学习

cast = ['A', 'B', 'C', 'D']
cast.append('E')
print(cast)
cast.pop()
print(cast)
cast.extend(['F', 'G'])
print(cast)
cast.remove('C')
print(cast)
cast.insert(0, 'C')
print(cast)

movies = ['The Holy Grail', 'The Life of Brian',
		  'The Meaning of Life']
movies.insert(1,1975)
movies.insert(3,1979)
movies.insert(5,1983)
print(movies)

movies = ['The Holy Grail', 1975, 'The Life of Brian',
		  1979, 'The Meaning of Life', 1983]
print(movies)

fav_movies = ['The Holy Grail', 'The Life of Brain']

print(fav_movies[0])
print(fav_movies[1])

for each_flick in fav_movies:
	print(each_flick)
print('\n')

movies = ['The Holy Grail', 1975, 'Terry Jones & Terry Gilliam', 91, ['Graham Chapman', ['Michael Palin', 'John Cleese',
																						 'Terry Gilliam', 'Eric Idle', 'Terry Jones']]]
for each_item in movies:
	if isinstance(each_item, list):
		for each in each_item:
			if isinstance(each, list):
				for ee in each:
					print(ee)
			else:
				print(each)
	else:
		print(each_item)

print('\n')

def print_lol(the_list):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item)
		else:
			print(each_item)
print_lol(movies)
print('\n')
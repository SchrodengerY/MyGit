# 腌制数据，pickle库的用法

import pickle

with open('mydata.pickle', 'wb') as mysavedata:
	pickle.dump([1,2,'three'],  mysavedata)

with open('mydata.pickle', 'rb') as myrestoredata:
	a_list = pickle.load(myrestoredata)

print(a_list)
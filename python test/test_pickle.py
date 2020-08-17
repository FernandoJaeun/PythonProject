import pickle
# f = open("test3.txt", 'wb')
# data = {1: 'python', 2: 'you need'}
# pickle.dump(data, f)
# f.close()

data = {1: 'python', 2: 'you need', 3: 'right now'}

with open("test3.txt", "wb") as pickle_file:
    pickle.dump(data, pickle_file)

with open("test3.txt", 'rb') as pickle_file2:
    data2 = pickle.load(pickle_file2)
    print(data2)
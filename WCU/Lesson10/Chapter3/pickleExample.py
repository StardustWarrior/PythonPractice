import pickle
from Time import Time
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'data.txt')

#Pickle to the terminal
myTime1 = Time(1, 2, 3)
pickled_time = pickle.dumps(myTime1)
print (pickled_time)

pickled_time = pickle.dumps(myTime1)
unpickled_time = pickle.loads(pickled_time)
unpickled_time.print_time()

#Pickle to a file
out_file = open(file_path, 'wb')
pickled_time = pickle.dump(myTime1, out_file)
out_file.close()
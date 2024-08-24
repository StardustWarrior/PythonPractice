import pickle
from Time import Time
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'data.txt')

in_file = open(file_path, 'rb')

unpickled_time = pickle.load(in_file)

unpickled_time.print_time()
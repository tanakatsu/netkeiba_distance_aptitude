# encoding: utf-8
import pickle
from argparse import ArgumentParser


def load_file(filename):
    with open(filename, 'r') as f:
        data = pickle.load(f)
    return data

parser = ArgumentParser()
parser.add_argument('file', action='store', type=str, help='input filename')

args = parser.parse_args()

input_data = load_file(args.file)
sorted_data = sorted(input_data.items(), key=lambda x: -x[1])

for name, score in sorted_data:
    print name.encode('utf-8'), score

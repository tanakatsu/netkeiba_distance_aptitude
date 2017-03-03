# encoding: utf-8
from argparse import ArgumentParser
import os
import pickle
from time import sleep
import netkeiba


def load_file(filename):
    with open(filename, 'r') as f:
        data = pickle.load(f)
    return data


def save_file(filename, data):
    with open(filename, 'w') as f:
        pickle.dump(data, f)


parser = ArgumentParser()
parser.add_argument('--input', '-i', action='store', type=str, required=True, help='input filename')
parser.add_argument('--key', '-k', action='store', type=str, default='name', help='key of dictionary')
parser.add_argument('--output', '-o', action='store', type=str, default='result.pkl', help='output filename')

args = parser.parse_args()

input_data = load_file(args.input)
names = [x[args.key] for x in input_data]
tmpfile = 'result.tmp.pkl'

netkeiba = netkeiba.Netkeiba()
data = {}
if os.path.exists(args.output):
    data = load_file(args.output)
elif os.path.exists(tmpfile):
    data = load_file(tmpfile)
count = len(data)

for name in names:
    processed_names = data.keys()
    if name not in processed_names:
        print len(data) + 1, ':', name
        html = netkeiba.searchHorseByName(name)
        if html:
            factor = netkeiba.getHorseDistanceAptitude(html)
            print name, factor
            data[name] = factor

            count = len(data)
            if count % 50 == 0:
                print 'Saved temporal file (count=%d)' % count
                save_file('result.tmp.pkl', data)
            sleep(0.1)
        else:
            print 'WARN: %s is not found' % name

save_file(args.output, data)

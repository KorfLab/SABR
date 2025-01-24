import argparse
import gzip
from multiprocessing import Pool
import os
import sys

from toolbox import FTX, readfasta

def run(a):
	genome, fasta = a
	return f'{genome}:{fasta}'


parser = argparse.ArgumentParser(description=f'threaded est2genome')
parser.add_argument('genome', help='genome file in FASTA format')
parser.add_argument('reads', help='reads file in FASTA format')
parser.add_argument('-t', '--threads', type=int, default=1,
	help='number of threads [%(default)i]')
arg = parser.parse_args()


with Pool(5) as p:
	print(p.map(run, [ ('g', 1), ('g', 2) , ('g', 3) ]))

# https://docs.python.org/3/library/multiprocessing.html#multiprocessing-programming

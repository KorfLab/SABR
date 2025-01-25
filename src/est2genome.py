import argparse
import gzip
from multiprocessing import Pool
import os
import sys

from toolbox import FTX, readfasta

def run(x):
	arg, pid, tid = x
	fasta = []
	ftx = []
	for i, (name, seq) in enumerate(readfasta(arg.reads)):
		if i % arg.threads != tid: continue
		rfa = f'{arg.build}/{pid}.{i}.fa'
		out = f'{arg.build}/{pid}.{i}.txt'
		with open(rfa, 'w') as fp: print(f'>{name}', seq, sep='\n', file=fp)
		os.system(f'est2genome -genomesequence {arg.genome} -estsequence {rfa} -outfile {out} 2>/dev/null')
		exons = []
		strand = None
		chrom = None
		with open(out) as fp:
			for line in fp:
				if line.startswith('Exon'):
					e, s, p, gb, ge, chrom, rb, re, rs = line.split()
					strand = rs[1]
					exons.append((int(gb), int(ge)))
		ftx = FTX(chrom, 'yo', strand, exons, '')
		print(ftx)
		

parser = argparse.ArgumentParser(description=f'threaded est2genome')
parser.add_argument('genome', help='genome file in FASTA format')
parser.add_argument('reads', help='reads file in FASTA format')
parser.add_argument('-x', '--extra', type=int, default=1000,
	help='extra sequence flanking guide HSPs [%(default)i]')
parser.add_argument('-t', '--threads', type=int, default=1,
	help='number of threads [%(default)i]')
parser.add_argument('-b', '--build', default='build',
	help='build directory for temp files [%(default)s]')
arg = parser.parse_args()

##########
# PART 1 # run blast to find the best chromosomal region
##########
os.system(f'mkdir -p {arg.build}')
os.system(f'cp {arg.genome} {arg.build}/genome.fa')
os.system(f'formatdb -p F -o T -i {arg.build}/genome.fa')
os.system(f'blastall -p blastn -d {arg.build}/genome.fa -i {arg.reads} -m 8 -a {arg.threads} -e 1e-10 > {arg.build}/est2.blastn')

# next
# parse blast report
# use fastacmd to get regions fastacmd -d build/genome.fa -s c1 -L 3,9

sys.exit()


##########
# PART 2 # run est2genome 
##########


run((arg, os.getpid(), 3))


"""
workers = [(arg, i) for i in range(arg.threads)]

if __name__ == '__main__':
	with Pool(arg.threads) as p:
		print(p.map(run, workers))

"""

##########
# PART 3 # repair coordiantes and make ftx
##########
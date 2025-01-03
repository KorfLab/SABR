import argparse
import gzip
import json
import sys

from toolbox import FTX

def best_alignment(ref, text):
	if text == 'None': return None
	if '~' not in text: return FTX.parse(text)
	min_dist = 1e9
	min_ali = None
	for astr in text.split('~'):
		ali = FTX.parse(astr)
		s = ref.distance(ali)
		if s < min_dist:
			min_dist = s
			min_ali = ali
	return min_ali

parser = argparse.ArgumentParser(description='alignment evaluator')
parser.add_argument('files', nargs='+', help='run-aligner.py output files')
parser.add_argument('--basename', required=True,
	help='base name for various output files')
parser.add_argument('--minexon', type=int, default=20,
	help='minimum exon length for table3 [%(default)i]')
parser.add_argument('--experimental', action='store_true',
	help='special processing for the synthetic genome experiment')
parser.add_argument('--debug', action='store_true')
parser.add_argument('--verbose', action='store_true')
arg = parser.parse_args()

# Aggregate alignment data by reference read

fps = []
progs = []
for file in arg.files:
	if   file.endswith('.ftx.gz'): fp = gzip.open(file, 'rt')
	elif file.endswith('.ftx'):    fp = open(file)
	else: sys.exit(f'unexpected file {file}')
	fps.append(fp)
	progs.append(file[:file.index('.')])

data = {}
while True:
	lines = []
	for fp in fps: lines.append(fp.readline().rstrip().split())
	if len(lines[0]) == 0: break
	for prog, (ref, ali) in zip(progs, lines):
		if ref not in data: data[ref] = {}
		data[ref][prog] = ali

# Evaluate best alignments and gather summary stats
sumtable = [{}, {}, {}]
with open(f'{arg.basename}_details.txt', 'w') as details:
	for rstr in data:
		ref = FTX.parse(rstr)
		print(ref, file=details)
		for prog, astr in data[rstr].items():
			ali = best_alignment(ref, astr)
			if   ali is None:      r = 'unaligned'
			elif ref.matches(ali): r = 'match'
			elif ref.similar(ali): r = 'partial'
			else:                  r = 'wrong'
			print(f'\t{ali}\t{r}', file=details)
			if len(ref.exons) <= 3: t = sumtable[len(ref.exons) -1]
			if prog not in t: t[prog] = {}
			if r not in t[prog]: t[prog][r] = 0
			t[prog][r] += 1

# Write summary stats
categories = ('match', 'partial', 'wrong', 'unaligned')
for i, table in enumerate(sumtable):
	with open(f'{arg.basename}_table{i+1}.tsv', 'w') as fp:
		print('program\t', '\t'.join(categories), file=fp)
		for prog in table:
			print(prog, end='\t', file=fp)
			for cat in categories:
				if cat not in table[prog]: n = 0
				else: n = table[prog][cat]
				print(n, end='\t', file=fp)
			print(file=fp)

# More performance metrics...
# bowtie and bwa are suppressing some alignments? or only doing best?

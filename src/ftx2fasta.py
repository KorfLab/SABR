import argparse
import sys
from toolbox import FTX, generator

parser = argparse.ArgumentParser()
parser.add_argument('genome', help='genome file in FASTA format')
parser.add_argument('ftx', help='annotation in FTX format')
parser.add_argument('mrna', help='mRNA output file')
parser.add_argument('tmask', help='transcript-masked output file')
arg = parser.parse_args()

mrna = open(arg.mrna, 'w')
tmask = open(arg.tmask, 'w')

for chrom, seq, ftxs in generator(arg.genome, arg.ftx):
	mseq = list(seq)
	for ftx in ftxs:
		tx = []
		for beg, end in ftx.exons:
			tx.append(seq[beg:end+1])
			for i in range(beg, end+1):
				mseq[i] = 'N'
		tseq = ''.join(tx)
		print(f'>{ftx}', file=mrna)
		for i in range(0, len(tseq), 80):
			print(tseq[i:i+80], file=mrna)
	mseq = ''.join(mseq)
	print(f'>{chrom}', file=tmask)
	for i in range(0, len(mseq), 80):
		print(mseq[i:i+80], file=tmask)

mrna.close()
tmask.close()

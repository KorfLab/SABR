
import sys
from toolbox import FTX, generator

if len(sys.argv) != 3: sys.exit(f'usage: python3 {sys.argv[0]} <genome> <ftx>')

for chrom, seq, ftxs in generator(sys.argv[1], sys.argv[2]):
	print(chrom, len(seq), len(ftxs))
	# unfinished

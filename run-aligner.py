import argparse
import gzip
import os
import sys

from toolbox import FTX, sam_to_ftx, readfasta

def run(cli, arg):
	cli = cli.replace('\t', ' ')
	cli = '/usr/bin/time -f "BAKETIME %M %U %S %E" ' + cli
	print(cli, file=sys.stderr)
	os.system(cli)

def needfastq(arg):
	fastq = f'{arg.reads[0:arg.reads.find(".")]}.fq.gz'
	if not os.path.exists(fastq):
		with gzip.open(fastq, 'wt') as fp:
			for name, seq in readfasta(arg.reads):
				print('@', name, file=fp, sep='')
				print(seq, file=fp)
				print('+', file=fp)
				print('J' * len(seq), file=fp)
	return fastq

def needfasta(arg):
	fasta = arg.reads[:-3]
	if not os.path.exists(fasta): os.system(f'gunzip -k {arg.reads}')
	return fasta

def samfile_to_ftxstream(filename, out, name):
	for ftx in sam_to_ftx(filename, info=name):
		print(ftx, file=out)

def sim4file_to_ftxstream(filename, out, name):
	chrom = None
	strand = None
	exons = []
	ref = None
	n = 0
	with open(filename) as fp:
		for line in fp:
			if line.startswith('seq1 ='):
				if chrom is not None:
					ftx = FTX(chrom, str(n), strand, exons,
						f'{arg.program}~{ref}')
					print(ftx, file=out)
				chrom = None
				strand = None
				exons = []
				ref = line[7:].split(' ')[0][:-1]
				n += 1
				continue
			elif line.startswith('seq2 ='):
				f = line.split()
				chrom = f[2][:-1]
				continue
			f = line.split()
			if len(f) != 4: continue
			beg, end = f[1][1:-1].split('-')
			exons.append((int(beg) -1, int(end) -1))
			st = '+' if f[3] == '->' else '-'
			if strand is None: strand = st
			else: assert(strand == st)
		ftx = FTX(chrom, str(n), strand, exons, f'{name}~{ref}')
		print(ftx, file=out)

#######
# CLI #
#######

parser = argparse.ArgumentParser(description='spliced alignment evaluator: '
	+ ', '.join(('blat', 'bowtie2', 'bwa-mem', 'gmap', 'hisat2',
	'magicblast', 'minimap2', 'star', 'tophat2')))
parser.add_argument('genome', help='genome file in FASTA format')
parser.add_argument('reads', help='reads file in FASTA format')
parser.add_argument('program', help='program name')
parser.add_argument('--threads', type=int, default=1,
	help='number of threads if changeable [%(default)i]')
parser.add_argument('--debug', action='store_true',
	help='keep temporary files (e.g. SAM)')
arg = parser.parse_args()

###############
# Run Aligner #
###############

out = f'temp-{os.getpid()}' # temporary output file
ftx = f'ftx-{os.getpid()}'  # temporary ftx file
fp = open(ftx, 'w')

if arg.program == 'blat':
	cli = f'blat {arg.genome} {arg.reads} {out} -out=sim4'
	run(cli, arg)
	sim4file_to_ftxstream(out, fp, arg.program)
elif arg.program == 'bowtie2':
	if not os.path.exists(f'{arg.genome}.1.bt2'):
		cli = f'bowtie2-build {arg.genome} {arg.genome}'
		run(cli, arg)
	fastq = needfastq(arg)
	cli = f'bowtie2 -x {arg.genome} -U {fastq} > {out}'
	run(cli, arg)
	samfile_to_ftxstream(out, fp, arg.program)
elif arg.program == 'bwa-mem':
	if not os.path.exists(f'{arg.genome}.bwt'):
		cli = f'bwa index {arg.genome}'
		run(cli, arg)
	cli = f'bwa mem {arg.genome} {arg.reads} > {out}'
	run(cli, arg)
	samfile_to_ftxstream(out, fp, arg.program)
elif arg.program == 'gmap':
	if not os.path.exists(f'{arg.genome}-gmap'):
		cli = f'gmap_build -d {arg.genome}-gmap -D . {arg.genome}'
		run(cli, arg)
	cli = f'gunzip -c {arg.reads} | gmap -d {arg.genome}-gmap -D . -f samse -t {arg.threads} > {out}'
	run(cli, arg)
	samfile_to_ftxstream(out, fp, arg.program)
elif arg.program == 'hisat2':
	if not os.path.exists(f'{arg.genome}.1.ht2'):
		cli = f'hisat2-build -f {arg.genome} {arg.genome}'
		run(cli, arg)
	cli = f'hisat2 -x {arg.genome} -U {arg.reads} -f -p {arg.threads} > {out}'
	run(cli, arg)
	samfile_to_ftxstream(out, fp, arg.program)
elif arg.program == 'magicblast':
	# notes: renames the chromosomes as numbers, maybe fix?
	if not os.path.exists(f'{arg.genome}.nsq'):
		cli = f'makeblastdb -dbtype nucl -in {arg.genome}'
		run(cli, arg)
	cli = f'magicblast -db {arg.genome} -query {arg.reads} -num_threads {arg.threads} > {out}'
	run(cli, arg)
	samfile_to_ftxstream(out, fp, arg.program)
elif arg.program == 'minimap2':
	cli = f'minimap2 -ax splice {arg.genome} {arg.reads} -t {arg.threads} > {out}'
	run(cli, arg)
	samfile_to_ftxstream(out, fp, arg.program)
elif arg.program == 'pblat':
	# reads need to be uncompressed (seekable)
	fasta = needfasta(arg)
	cli = f'pblat {arg.genome} {fasta} {out} -threads={arg.threads} -out=sim4'
	run(cli, arg)
	sim4file_to_ftxstream(out, fp, arg.program)
elif arg.program == 'star':
	idx = f'{arg.genome}-star'
	if not os.path.exists(idx):
		cli = f'STAR --runMode genomeGenerate --genomeDir {idx}\
			--genomeFastaFiles {arg.genome} --genomeSAindexNbases 8'
		run(cli, arg)
	cli = f'STAR --genomeDir {idx} --readFilesIn {arg.reads} --readFilesCommand "gunzip -c" --outFileNamePrefix {out} --runThreadN 1'
	run(cli, arg)
	os.rename(f'{out}Aligned.out.sam', f'{out}')
	for x in ('Log.final.out', 'Log.out', 'Log.progress.out', 'SJ.out.tab'):
		os.unlink(f'{out}{x}')
	samfile_to_ftxstream(out, fp, arg.program)
elif arg.program == 'tophat2':
	if not os.path.exists(f'{arg.genome}.1.bt2'):
		cli = f'bowtie2-build {arg.genome} {arg.genome}'
		run(cli, arg)
	cli = f'tophat2 -p {arg.threads} {arg.genome} {arg.reads} '
	run(cli, arg)
	cli = f'samtools view -h tophat_out/accepted_hits.bam > {out}'
	run(cli, arg)
	samfile_to_ftxstream(out, fp, arg.program)
	if not arg.debug: os.system('rm -rf tophat_out')
else:
	sys.exit(f'ERROR: unknown program: {arg.program}')

fp.close()

#####################
# Report Alignments #
#####################

refs = [name for name, seq in readfasta(arg.reads)]
aligned = {}
with open(ftx) as fp:
	for line in fp:
		ali, ref = line.rstrip().split('~')
		if ref not in aligned: aligned[ref] = ali
		else: aligned[ref] += '~' + ali # chaining extra alignments

with gzip.open(f'{arg.program}.ftx.gz', 'wt') as fp:
	for ref in refs:
		if ref in aligned: print(ref, aligned[ref], sep='\t', file=fp)
		else:              print(ref, 'None', sep='\t', file=fp)

############
# Clean up #
############

if not arg.debug and os.path.exists(out): os.unlink(f'{out}')
if not arg.debug and os.path.exists(ftx): os.unlink(f'{ftx}')

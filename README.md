Spliced Alignment Bakeoff
=========================

Aligning transcript (mRNA) sequences to their genomic source locations is a
surprisingly difficult problem. This project seeks to answer the following
questions:

- Which is the most accurate aligner for RNA-seq data?
- What kinds of sequence and gene features create the most problems?
- What improvements can be made in spliced alignment?

Preprint: ___
Reference: ___

## Quickstart ##

1. Install conda
2. Clone the repo
3. Create the environment
4. Run the demo

Disclaimer: This project was designed, tested, and executed in an x86-linux
environment. It may be possible to run outside this context. We may provide
future support in this area, but not yet.

You must install some flavor of conda. We typically use Miniforge3. After conda
has been installed and you are in the base environment, you may start the next
steps.

```
git clone https://github.com/KorfLab/spliced-alignment-bakeoff
cd spliced-alignment-bakeoff
conda env create -f env.yml
conda activate bakeoff
./bakeoff -ts1 data/ce01.fa data/ce01.ftx build pblat minimap2
```

## Manifest ##

- `README.md` this document
- `env.yml` conda environment
- `bakeoff` top-level wrapper program
- `data/` directory with some sample files (1% of favorite genomes)
- `compare-alignments.py` evaluates performance of aligners
- `genome-simulator.py` creates an experimental genome and annotation
- `read-simulator.py` creates synthetic RNA-seq reads from FASTA + GFF
- `run-aligner.py` provides a consistent interface to multiple programs
- `toolbox.py` shared library for the project
- `sam2ftx.py` for conversion outside the bakeoff context (e.g. dragen)
- `gff2ftx.py` for converting gff to ftx (requires KorfLab/grimoire)

## Flattened Transcript Format ##

This project uses a custom file format to embed exon-intron structure in
FASTA/FASTQ identifiers. It is not intended to be used outside this study.

- file extension: `.ftx` (not an official file extension)
- field delimiter: `|`
- 5 fields

1. chromosome identifier
2. name of transcript
3. strand indicator `+` or `-`
4. exon structure:
	- hyphen separated coordinates
	- comma separated exons
	- must be sorted left to right, low to high
	- numbers are 1-based
5. information: optional extra free text

Example: Plus-strand transcript with introns at 201-299 and 401-499 and no
extra information.

```
chr1|gene-1|+|100-200,300-400,500-600|
```

Example: Minus-strand transcript with some extra info.

```
chr2|gene-2|-|100-200,300-400,500-600|extra free text
```

## TO DO ##


- real genomes
	- have masking, what to do about that?
	- what about a large genome?
- big runs
- analysis

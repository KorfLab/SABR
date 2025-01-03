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

This project was designed, tested, and executed in an x86-linux environment. It
may be possible to run outside this context. We may provide future support in
this area, but not yet.

1. Install conda (e.g. Miniforge3)
2. Clone this repo
3. Create the conda environment from `env.yml`
4. Run the demos in the `bakeoff` usage statement

See the `TUTORIAL.md` for a step-by-step walkthrough.

## Manifest ##

- `README.md` this document
- `env.yml` conda environment
- `bakeoff` top-level program for running analyses
- `data/` directory with some sample files (1% of favorite genomes)
- `compare-alignments.py` evaluates performance of aligners
- `genome-simulator.py` creates an experimental genome and annotation
- `read-simulator.py` creates synthetic RNA-seq reads from FASTA + GFF
- `run-aligner.py` provides a consistent interface to multiple programs
- `toolbox.py` shared library for the project
- `sam2ftx.py` for conversion outside the bakeoff context (e.g. dragen)
- `gff2ftx.py` for converting gff to ftx (requires KorfLab/grimoire)

## Flattened Transcript Format ##

This project uses a custom file format to serialize gene structure annotation
into a single token for embedding in FASTA/FASTQ identifiers. It is not
intended to be used outside this study.

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

Example: The information field can contain another ftx. A `~` is used to show
the 2nd ftx. This is used within the bakeoff to attach a genomic source to all
of its alignments (an aligner may provide more than one alignment).

```
chr1|gene-1|+|100-200,300-400,500-600|~chr1|gene-1|+|100-200,300-400,500-600|
```

## TO DO ##

- check all mis-alignments for sam issues
- real genomes
	- have masking, what to do about that?
	- what about a large genome?
- big runs
- analysis

README: Spliced Alignment Bakeoff
=================================

Aligning transcript (mRNA) sequences to their genomic source locations is a
surprisingly difficult problem. This project seeks to answer the following
questions:

- Which is the most accurate aligner for RNA-seq data?
- What kinds of sequence and gene features create the most problems?
- What improvements can be made in spliced alignment?

Preprint: ___

Reference: ___

## Quickstart ##

This project was designed, tested, and executed in an x86-linux environment.
Running outside this environment may take some adjustments.

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
- `dev/` directory with some programs used in development & debugging
- `compare-alignments.py` evaluates performance of aligners
- `genome-simulator.py` creates an experimental genome and annotation
- `read-simulator.py` creates synthetic RNA-seq reads from FASTA + GFF
- `run-aligner.py` provides a consistent interface to multiple programs
- `toolbox.py` shared library for the project

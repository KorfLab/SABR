README: Spliced Alignment Benchmarking Resource
===============================================

Aligning transcripts to their genomic source locations is a surprisingly
difficult problem. This project seeks to answer the following questions:

- Do aligners fail some simple sanity checks?
- Which aligner is the most accurate?
- Which aligner is the most efficient?
- What kinds of sequence and gene features create the most problems?
- What improvements can be made in spliced alignment?

## Quickstart ##

1. Install conda (e.g. Miniforge3)
2. Clone this repo
3. Create conda environment
4. Run the demos in the `bakeoff` usage statement

See the `TUTORIAL.md` for a step-by-step walkthrough.

## Manifest ##

- `README.md` this document
- `TUTORIAL.md` a quick walk-through to check that things work
- `INFO.md` some behind-the-scenes information
- `NOTES.md` random stuff the devs are thinking about or working on
- `bakeoff` top-level program for assessing aligners
- `env/` directory of conda environments for different platforms
- `data/` directory with some sample files (1% of favorite genomes)
- `src/` directory with programs that run various parts of the analyses
- `2025/` directory with specifics for the 2025 study

## estgenome ##

Testing

```
conda activate sabr-linux-x86
python3 src/read-simulator.py data/ce01.fa.gz data/ce01.ftx.gz --seed 1 --samplegene 0.05 --samplereads 0.01 > rtest.fa
python3 src/est-genome.py data/ce01.fa.gz rtest.fa --verbose
```
Runnning

- Remove `--verbose`` flag
- Add `--threads n` for however many CPUs you are using
- Remove `temp` directory (it doesn't auto-delete for debugging reasons)

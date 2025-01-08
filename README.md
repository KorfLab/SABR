README: Spliced Alignment Bakeoff
=================================

Aligning RNA-seq reads to their genomic source locations is a surprisingly
difficult problem. This project seeks to answer the following questions:

- Which is the most accurate aligner for RNA-seq data?
- What kinds of sequence and gene features create the most problems?
- What improvements can be made in spliced alignment?
- Do aligners fail some simple sanity checks?

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
- `TUTORIAL.md` a quick walk-through to check that things work
- `INFO.md` some behind-the-scenes information
- `NOTES.md` random stuff the devs are thinking about or working on
- `env.yml` conda environment
- `bakeoff` top-level program for running a bakeoff
- `data/` directory with some sample files (1% of favorite genomes)
- `src/` directory with programs that run various parts of the bakeoff
- `2025/` directory with specifics for the 2025 study

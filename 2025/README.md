2025 Alignment Bakeoff
======================

Goals

- Sanity checks
- Short reads
- Synthetic reads
- Synthetic and miniaturized model organism genomes

Future Studies

- Mutated reads
- Long reads
- Real reads
- Larger genomes

## Checksum Data Files ##

To ensure that the genome data and reads are exactly as expected, you might
want to checksum the bakeoff data files and the reads that are generated.

```
./bakeoff -mts1 data/ce01.fa.gz data/ce01.ftx.gz build
```

| File        | MD5
|:------------|:---------------------------------
| genome.fa   | 019858da7aa6fa25a6d8ccf4284688eb
| genome.ftx  | 0b7ccd51452d8829343ebb8a8b302698
| reads.fa.gz | bf16185f7da58ced68f4631e37cd78bd


## Paralogy & Repeats ##

All regions of transcript-similarity are in paralogy.txt

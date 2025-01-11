NOTES: Spliced Alignment Benchmarking Resource
==============================================

## Sanity checks ##

- version name is the same as reported in conda
- software produces the same output when run multiple times
- software produces the same output on multiple architectures
- single and multiple cpus give the same answer
- plus and minus strand have the exact same results
- names, seqs, quality values are not mutated

## Insanity Notes ##

- hisat2 sometimes makes really short exons instead of a single alignment
- minimap2 sometimes aligns + and - reads differently
- magicblast changes program names
- some program is increasing quality values in sam format

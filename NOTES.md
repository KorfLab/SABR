NOTES: Spliced Alignment Bakeoff
================================

Project lead should contact the authors to get their best parameters for
accurate spliced alignment.

- bbmap
- blat
- bowtie2 - doesn't do spliced alignment, no point in contacting
- bwa - doesn't do spliced alignment, no point in contacting
- gem3-mapper
- gmap
- hisat2
- magicblast
- minimap2
- novoalign - contacted to obtain license and get best parameters
- pblat
- segemehl
- star
- subread
- tophat

Real genomes have repeats. Do any of the exons overlap repeats? Might want to
do the whole study with clean and masked sequence.

Real genomes have duplications. It can therefore be impossible to locate the
correct alignment. Should we try to identify regions of identity at the outset?

Sanity checks

- plus and minus strand have the exact same results
- single and multiple cpus give the same answer
- names are preserved (e.g. chromsosomes)

Alignment Notes

- hisat2 sometimes makes really short exons instead of a single alignment
- minimap2 sometimes aligns + and - reads differently
- maybe need automated discrepancy checkers

When aligners all agree, the alignemtn is probably robust. When they disagree,
it's time to look deeper.

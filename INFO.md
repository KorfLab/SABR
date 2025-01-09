INFO: Spliced Alignment Bakeoff
===============================

## Flattened Transcript Format ##

This project uses a custom file format to serialize gene structure annotation
into a single token for embedding in FASTA/FASTQ identifiers. It is not
intended to be used outside this study.

- file extension: `.ftx` (not an official file extension)
- field delimiter: `|`
- 5 fields
- no spaces in fields 1-4

1. chromosome identifier
2. name of gene/transcript/read/whatever
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

## Regression Testing ##

To ensure that the genome data and reads are exactly as expected, you might
want to checksum the bakeoff data files.

```
./bakeoff -mts1 data/ce01.fa.gz data/ce01.ftx.gz build
```

| File        | MD5
|:------------|:---------------------------------
| genome.fa   | 019858da7aa6fa25a6d8ccf4284688eb
| genome.ftx  | 0b7ccd51452d8829343ebb8a8b302698
| reads.fa.gz | bf16185f7da58ced68f4631e37cd78bd

Checksumming the alignments is another issue...

- different versions in different environments
- parallel processing
- updated software
- program reports something different from conda
- mmap failures on OSX
- outside of x86-linux, shit isn't going to work

## Synthetic Genomes & Reads ##

The `genome-simulator.py` program creates a 3-exon gene whose middle exon has
variable length. A text-glyph is shown below. By default, all introns follow
the GT-AG rule.

```
~~~[exon]--intron--[var.exon]--intron--[exon]~~~
```

Passing the `--double`` flag creates genes on both strands and the
`--noncanonical` flag creates introns with additional splice sites: GC-AG,
AT-AC, and AA-TT (AA-TT is used to represent _other_ not an acutal splice
site).

The `read-simulator.py` program generates reads along the entire length of a
gene's mRNA. The `--double` flag creates reads from both strands.

```
[exon][var.exon][exon]
------ ------ ------
 ------ ------ ------
  ------ ------ ------
   ------ ------
    ------ ------
     ------ ------
      ------ ------
```

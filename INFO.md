INFO: Spliced Alignment Bakeoff
===============================

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

## Regression Testing ##

Alignment software changes from time to time, so the results of a bakeoff might
also change.

Some algorithms may produce alignments in different orders when the number of
processors is changed. This causes a difference in the checksum but not the
actual alignments. When testing, use a single processor (the `bakeoff`
default). Later, you may want to reduce elapsed time with `-p4` for 4
processors (threads).

The Version below is what is reported in conda, not what the program reports.
They may be different.

When you run `md5sum`, make sure you run it via stdin because files that have
been gzipped may contain metadata that artificially makes the contents of two
gzipped files look different.

```
gunzip -c build/pblat.ftx.gz | md5sum
```

With all of those caveats in place, here are the checksums for the various
programs run with `bakeoff -ts1 data/ce* ...`

| Program    | Version    | MD5
|:-----------|:-----------|:--------------------------------
| blat       | 35         |
| bowtie2    | 2.2.5      |
| bwa-mem    | 0.7.18     |
| gmap       | 2024.11.20 |
| hisat2     | 2.2.0      |
| magicblast | 1.7.0      |
| minimap2   | 2.28       |
| pblat      | 2.5.1      |
| star       | 2.7.11a    |
| tophat2    | 2.1.1      |


## Synthetic Genomes & Reads ##

The `genome-simulator.py` program creates a 3-exon gene whose middle exon has
variable length.

```
~~~[exon]--intron--[var.exon]--intron--[exon]~~~
```

Passing the `--double`` flag creates genes on both strands and the
`--noncanonical` flag creates introns with additional splice sites.

The `read-simulator.py` program generates reads along the entire length of a
gene's mRNA.

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

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

To ensure that the genome data and reads are exactly as expected, checksum the
bakeoff data files.

```
./bakeoff -mts1 data/ce01.fa.gz data/ce01.ftx.gz build
```

| File        | MD5
|:------------|:---------------------------------
| genome.fa   | 019858da7aa6fa25a6d8ccf4284688eb
| genome.ftx  | 0b7ccd51452d8829343ebb8a8b302698
| reads.fa.gz | bf16185f7da58ced68f4631e37cd78bd


Alignment software changes from time to time, so the results of a bakeoff might
also change.

Some algorithms may produce alignments in different orders when the number of
processors is changed. This causes a difference in the checksum but not the
actual alignments. When testing, use a single processor (the default). Later,
you may want to reduce elapsed time, so add `-p4` for 4 processors (threads) or
however many you like, but note that memory usage with some programs may become
excessive.

The program versions shown below are what `conda env export` reports, and not
necessarily what the program reports.

With those caveats in place, we can checksum the blat and star outputs with the
following command.

```
./bakeoff -mts1 data/ce01.fa.gz data/ce01.ftx.gz build blat star
```

Here's the table of MD5s used in the paper ...

| Abbr | Program     | Conda      | MD5
|:-----|:------------|:-----------|:--------------------------------
| bbmp | bbmap       | 39.01      | 2c4f61dd3b606ec1e0ed91852ad6aaa9
| blat | blat        | 35         | 8aed9d45ec270798bdbc4da5a7bb66f8
| bow2 | bowtie2     | 2.2.5      | 92042c69570254936a7424ccf5851355
| bwam | bwa-mem     | 0.7.18     | 8ccf22c881c72fa368f8f646150cbebc
| gem3 | gem3-mapper | 3.6.1      | 807bc76bec974ccc68556ece73c4c0f7
| gmap | gmap        | 2024.11.20 | c8eab56b09e6c55f53a334b4dd470a5c
| hst2 | hisat2      | 2.2.0      | 9144fb25a43c4cac71e3d54a8db466a9
| magi | magicblast  | 1.7.0      | 1394c3d3c6077d319046b41ebd8d093e
| min2 | minimap2    | 2.28       | 47921c827e614290d64609b7275a9aba
| novo | novoalign   | 4.03.04    |
| pblt | pblat       | 2.5.1      | 8aed9d45ec270798bdbc4da5a7bb66f8
| sege | segemehl    | 0.3.4      | 29a11fef7edd7e696accfa325076a638
| star | star        | 2.7.11a    | ee09b00cbb8b07be2d5a1a5fa28d6ae1
| subr | subread     | 2.0.6      | 6ef20af10bfbe8d4b4e2bf84fe62e86f
| top2 | tophat2     | 2.1.1      | 530e0f92cc4674f4662177f01826fa30

## Resource Usage ##

Redirect the output and grep BAKEOFF in the log
Probably best to use a VM with a single cpu

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

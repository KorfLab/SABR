Tutorial
========

## Installation ##

You must install some flavor of conda. We typically use Miniforge3. After conda
has been installed and you are in the base environment, you may start the next
steps.

```
git clone https://github.com/KorfLab/spliced-alignment-bakeoff
cd spliced-alignment-bakeoff
conda env create -f env.yml
conda activate bakeoff
./bakeoff
```

The `bakeoff` usage statement provides 2 example command lines. We are going to
use those. But first, some explanations.

## Data ##

If you look in the `data` directory, you will see several files. These
represent subsets of various genomes. For example `ce01.fa.gz` contains the
first 1 percent of each chromosome of C. elegans. There is a companion gene
annotation file `ce01.ftx.gz` that contains the exon-intron coordinates of
genes in FTX format (see below).

```
ls data
zless data/ce01.fa.gz
zless data/ce01.ftx.gz
```

## Bakeoff ##

The `-t` flag puts `bakeoff` into test mode. This samples 10% of the genes and
10% of the reads. Without the `-t` flag, reads are generated from every gene at
every position.

The `-s` flag sets the random seed. This is useful for reproducing a study or
for checking that the software works as expected. `-s1` sets the seed to 1.
`-ts1` sets both the testing flag and the seed. This is synonymous with the
longer format `-t -s 1`.

Run the command below, which specifies the data files, a directory where the
work will be done, `build`, and the aligners to use, `pblat` and `minimap2`.
You will see a few status messages in the terminal as the aligners run. Each
aligner spews various messages to stdout or stderr.

```
./bakeoff -ts1 data/ce01.* build pblat minimap2
```

Examine the output files in the `build` directory.

```
zless build/pblat.ftx.gz
zless build/minimap2.ftx.gz
```

Let's look at the 2nd example command line. The `-f` flag forces the aligners
to run again and overwrite the output files. The cryptic  `> log.txt 2>&1` at
the end of the line writes both stdout and stderr to a `log.txt` file.

```
./bakeoff -fts1 data/ce01.* build pblat minimap2 > log.txt 2>&1
```

Redirecting the output serves two purposes: (1) the terminal is less noisy (2)
you can look at the resources (memory, time (user, system, elapsed)) consumed
by each program by searching for the word `BAKETIME`.

```
grep BAKETIME log.txt
```

## Unfinished ##

- Checksum the output...
- Alignment comparisons...

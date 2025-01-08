Tutorial: Spliced Alignment Bakeoff
===================================

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

## Genome Data ##

If you look in the `data` directory, you will see several files. These
represent subsets of various genomes. For example `ce01.fa.gz` contains the
first 1 percent of each chromosome of C. elegans. There is a companion gene
annotation file `ce01.ftx.gz` that contains the exon coordinates of genes in
FTX format (see `INFO.md`).

```
ls data
zless data/ce01.fa.gz
zless data/ce01.ftx.gz
```

## Test Bakeoff ##

The `-t` flag puts `bakeoff` into test mode. This samples 10% of the genes and
10% of the reads. Without the `-t` flag, reads are generated from every gene at
every position of the mRNA.

The `-s` flag sets the random seed. This is useful for reproducing a study or
for checking that the software works as expected. `-s1` sets the seed to 1.
`-ts1` sets both the testing flag and the seed. This is synonymous with the
longer format `-t -s 1`.

Run the command below, which specifies the data files, a directory where the
work will be done, `build`, and the aligners to use, `blat` and `star`. You
will see a few status messages in the terminal as the aligners run. Each
aligner spews various messages to stdout or stderr.

```
./bakeoff -ts1 data/ce01.* build blat star
```

Examine the output files in the `build` directory.

```
zless build/blat.ftx.gz
zless build/star.ftx.gz
```

Let's look at the 2nd example command line. The `-f` flag forces rewrite. The
`-m` flag reports MD5 checksums for the data files and program outputs. The
cryptic  `> log.txt 2>&1` at the end of the line writes both stdout and stderr
to a `log.txt` file. You may like to grep that later for BAKEOFF.

```
./bakeoff -fmts1 data/ce01.* build pblat minimap2 > log.txt 2>&1
grep BAKEOFF log.txt
```

For a more complete test, examine and then run `test-bakeoff.sh`.

```
cat test-bakeoff.sh
sh test-bakeoff.sh
```

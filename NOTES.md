NOTES: Spliced Alignment Bakeoff
================================

## Contact Authors for Best Parameters ##

Probably should do the whole thing with both optimized and default parameters.

- bbmap
- blat
- bowtie2 - doesn't do spliced alignment, no point in contacting
- bwa - doesn't do spliced alignment, no point in contacting
- gem3-mapper
- gmap
- hisat2
- magicblast
- minimap2
- pblat
- segemehl
- star
- subread
- tophat

## Real Genome Issues ##

- All regions of transcript-similarity are in paralogy.txt
- Check for N's in any of the exons. There are none.

## Sanity checks ##

- plus and minus strand have the exact same results
- single and multiple cpus give the same answer
- same thing run twice has the same answer (md5)
- names are preserved (e.g. chromsosomes, not in magicblast)

## Alignment Notes ##

- hisat2 sometimes makes really short exons instead of a single alignment
- minimap2 sometimes aligns + and - reads differently
- maybe need automated discrepancy checkers

When aligners all agree, the alignemtn is probably robust. When they disagree,
it's time to look deeper.


## Resources ##

Something like this will go in supplementary information. Also memory usage.
Not sure /usr/bin/time agglomerates children though.

Single CPU VM, single CPU run

```
./bakeoff -dmts1 data/ce* build bbmp blat bow2 bwam gem3 gmap hst2 magi min2 pblt sege star subr top2 > log.txt 2>&1
grep ELAPSED log.txt
BAKEOFF ELAPSED bbmp: 9.75312328338623
BAKEOFF ELAPSED blat: 0.21653413772583008
BAKEOFF ELAPSED bow2: 0.8180224895477295
BAKEOFF ELAPSED bwam: 0.35102367401123047
BAKEOFF ELAPSED gem3: 0.769636869430542
BAKEOFF ELAPSED gmap: 37.78698229789734
BAKEOFF ELAPSED hst2: 0.4799656867980957
BAKEOFF ELAPSED magi: 1.3995521068572998
BAKEOFF ELAPSED min2: 0.2736806869506836
BAKEOFF ELAPSED pblt: 0.1918020248413086
BAKEOFF ELAPSED sege: 1.705089807510376
BAKEOFF ELAPSED star: 0.5660688877105713
BAKEOFF ELAPSED subr: 4.627634286880493
BAKEOFF ELAPSED top2: 1.5509531497955322
```

Dual CPU VM, single CPU run

```
./bakeoff -dmts1 data/ce* build bbmp blat bow2 bwam gem3 gmap hst2 magi min2 pblt sege star subr top2 > log.txt 2>&1
grep ELAPSED log.txt
BAKEOFF ELAPSED bbmp: 7.4475603103637695
BAKEOFF ELAPSED blat: 0.2112283706665039
BAKEOFF ELAPSED bow2: 0.8618078231811523
BAKEOFF ELAPSED bwam: 0.3290235996246338
BAKEOFF ELAPSED gem3: 0.6376163959503174
BAKEOFF ELAPSED gmap: 38.40736699104309
BAKEOFF ELAPSED hst2: 0.4970576763153076
BAKEOFF ELAPSED magi: 2.2462239265441895
BAKEOFF ELAPSED min2: 0.26168251037597656
BAKEOFF ELAPSED pblt: 0.19622278213500977
BAKEOFF ELAPSED sege: 1.5973944664001465
BAKEOFF ELAPSED star: 0.5649058818817139
BAKEOFF ELAPSED subr: 5.033008813858032
BAKEOFF ELAPSED top2: 1.52274489402771
```


Dual CPU VM, dual CPU run

```
./bakeoff -dmts1 -p2 data/ce* build bbmp blat bow2 bwam gem3 gmap hst2 magi min2 pblt sege star subr top2 > log.txt 2>&1
grep ELAPSED log.txt
BAKEOFF ELAPSED bbmp: 6.295899152755737
BAKEOFF ELAPSED blat: 0.20643043518066406
BAKEOFF ELAPSED bow2: 0.7587707042694092
BAKEOFF ELAPSED bwam: 0.38596677780151367
BAKEOFF ELAPSED gem3: 0.6403162479400635
BAKEOFF ELAPSED gmap: 31.171127796173096
BAKEOFF ELAPSED hst2: 0.45430707931518555
BAKEOFF ELAPSED magi: 1.4106454849243164
BAKEOFF ELAPSED min2: 0.17597603797912598
BAKEOFF ELAPSED pblt: 0.13689446449279785
BAKEOFF ELAPSED sege: 1.008108139038086
BAKEOFF ELAPSED star: 0.5549609661102295
BAKEOFF ELAPSED subr: 4.749590158462524
BAKEOFF ELAPSED top2: 1.3473553657531738
```

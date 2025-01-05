NOTES: Spliced Alignment Bakeoff
================================

Stuff on a Saturday

- bbmp ftx assertion fail
- sege ftx assertion fail


Real genomes have duplications. It can therefore be impossible to locate the
correct alignment.

Sanity checks

- plus and minus strand have the exact same results
- single and multipe cpus give the same answer
- names are preserved (e.g. chromsosomes)


### ce01

- hisat2: 6 wrong (prefer to make a short intron and a splice)
- minimap2: 1 partial (+ and - strand alignments not the same)

hisat2 has 6 misalignments for single exons. In each case, a 1 bp exon was
preferred over a simple, single alignment.

ref:  I|Transcript:Y48G1C.6.1|-|84387-84486|r+
hisat2:  I|34583|+|84313-84313,84388-84486|

minimap2 has 1 misalignment. The plus strand read is aligned correctly, but
the minus strand read is not.

II|Transcript:C23H3.9d.1|-|77492-77591|r+       0       II      77492   60      100M    *       0       0       AGCGAAATTGTGCGTCGAGCTCCTTACCGCGCGGAAAAAGAAGCGCCCTGTGCAAAAGGGGCGGAGATTACAGTGTATGTGTGTGTGTGTGTGTGTGTGC    *       NM:i:0  ms:i:100        AS:i:100        nn:i:0  tp:A:P  cm:i:31 s1:i:98 s2:i:0  de:f:0  rl:i:0
II|Transcript:C23H3.9d.1|-|77492-77591|r-       16      II      77492   60      77M2D20M3S      *       0       0       AGCGAAATTGTGCGTCGAGCTCCTTACCGCGCGGAAAAAGAAGCGCCCTGTGCAAAAGGGGCGGAGATTACAGTGTATGTGTGTGTGTGTGTGTGTGTGC    *       NM:i:2  ms:i:93 AS:i:93 nn:i:0  tp:A:P  cm:i:30 s1:i:96 s2:i:0  de:f:0.0102     rl:i:0

### dm01

- hisat 1 partial, 7 wrong
	- wrong
		- 1 bp exon
		- 3 bp exon
		- 3 bp exon
		- 2 bp exon
		- 2 bp exon
		- 1 bp exon
		- 1 bp exon
	- partial
		- 1 bp exon
- minimap2: 2 partial, 3 wrong
	- wrong
		- minus missed
		- small deletion both strands
		- small deletion both strands
		- small deletion both strands

### at01

- blat 54 wrong
- gmap 92 wrong
- hisat 46 partia, 74 wrong
- minimap2 23 partial, 26 wrong
- pblat 54 wrong




### exp1


14720 total reads in each experiment
s1: hisat misses 2
s2: ok
s3: hisat misses 2



s1 hisat prefers to make a 5 nt exon and 50 nt intron

c8|9:GTAG|+|13268-13367|r+      0       c8      13218   60      5M50N95M        *        0       0       GTAACTACTTTAATTTCTACGCAAATCTTGACAGAAACCTCCGCAGTGCAGATTCTATCCACGCCGTGGATCAAACGTGGGCTACCCCTTTCATGTGTGC

c8|9:GTAG|+|13268-13367|r-      16      c8      13218   60      5M50N95M        *        0       0       GTAACTACTTTAATTTCTACGCAAATCTTGACAGAAACCTCCGCAGTGCAGATTCTATCCACGCCGTGGATCAAACGTGGGCTACCCCTTTCATGTGTGC


s3 hisat makes a 3 nt exon and 50 nt intron

c6|31:AATT|+|88415-88514|r+     0       c6      88365   60      3M50N97M        *        0       0       AAGTGGCTATCAGTACAGATAAATGATAGCTTAGACCGGAGACTGTCGCTTTCCCCGTCACTTATGTTGACACACATGGTGGCGTTCGCGTTGGTATTGA

c6|31:AATT|+|88415-88514|r-     16      c6      88365   60      3M50N97M        *        0       0       AAGTGGCTATCAGTACAGATAAATGATAGCTTAGACCGGAGACTGTCGCTTTCCCCGTCACTTATGTTGACACACATGGTGGCGTTCGCGTTGGTATTGA


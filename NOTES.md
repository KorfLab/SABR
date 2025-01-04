NOTES: Spliced Alignment Bakeoff
================================

Random notes

### ce01

single-exon misalignments

hisat2 has 6 misalignments for single exons. In each case, a 1 bp exon was
preferred over a simple, single alignment.

ref:  I|Transcript:Y48G1C.6.1|-|84387-84486|r+
hisat2:  I|34583|+|84313-84313,84388-84486|

minimap2 has 1 misalignment. The plus strand read is aligned correctly, but
the minus strand read is not.

II|Transcript:C23H3.9d.1|-|77492-77591|r+       0       II      77492   60      100M    *       0       0       AGCGAAATTGTGCGTCGAGCTCCTTACCGCGCGGAAAAAGAAGCGCCCTGTGCAAAAGGGGCGGAGATTACAGTGTATGTGTGTGTGTGTGTGTGTGTGC    *       NM:i:0  ms:i:100        AS:i:100        nn:i:0  tp:A:P  cm:i:31 s1:i:98 s2:i:0  de:f:0  rl:i:0
II|Transcript:C23H3.9d.1|-|77492-77591|r-       16      II      77492   60      77M2D20M3S      *       0       0       AGCGAAATTGTGCGTCGAGCTCCTTACCGCGCGGAAAAAGAAGCGCCCTGTGCAAAAGGGGCGGAGATTACAGTGTATGTGTGTGTGTGTGTGTGTGTGC    *       NM:i:2  ms:i:93 AS:i:93 nn:i:0  tp:A:P  cm:i:30 s1:i:96 s2:i:0  de:f:0.0102     rl:i:0

makes me wonder how many times plus/minus are done differently

### exp1



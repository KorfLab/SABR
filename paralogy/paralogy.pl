use strict;
use warnings 'FATAL' => 'all';

my @real = qw(at01 ce01 dm01);
foreach my $genome (@real) {
	`python3 ../src/ftx2fasta.py ../data/$genome.fa.gz ../data/$genome.ftx.gz $genome-mrna $genome-tmask` unless -s "$genome-mrna";
	`makeblastdb -in $genome-mrna -dbtype nucl` unless -s "$genome-mrna.nsq";
	`makeblastdb -in $genome-tmask -dbtype nucl` unless -s "$genome-tmask.nsq";
	`blastn -db $genome-mrna -query $genome-mrna > $genome-mm.blastn` unless -s "genome-mm.blastn";
	`blastn -db $genome-tmask -query $genome-mrna > $genome-tm.blastn` unless -s "genome-tm.blastn";
}


#blastn -db at01.mrna -query at01.mrna > at01.mrna.blastn
#blastn -db ce01.mrna -query ce01.mrna > ce01.mrna.blastn
#blastn -db dm01.mrna -query dm01.mrna > dm01.mrna.blastn

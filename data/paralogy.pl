use strict;
use warnings 'FATAL' => 'all';

`mkdir -p build`;
my @genome = qw(at01 ce01 dm01);
foreach my $genome (@genome) {
	`python3 ../src/ftx2fasta.py $genome.fa.gz $genome.ftx.gz > build/$genome-mrna`;
	`gunzip -c $genome.fa.gz > build/$genome.fa`;
	`makeblastdb -in build/$genome.fa -dbtype nucl`;
	`blastn -db build/$genome.fa -query build/$genome-mrna -evalue 1e-10 -perc_identity 95 -outfmt 6 > build/$genome.blastn`;
	report_paralogy("build/$genome.blastn");
}

sub report_paralogy {
	my $file = shift;
	print "\n$file\n";
	open(my $fh, $file) or die;
	my %match;
	while (<$fh>) {
		my ($q, $s, $pct, $al, $ms, $go, $qb, $qe, $sb, $se, $e, $b) = split;
		($sb, $se) = ($se, $sb) if $sb > $se;
		push @{$match{$q}}, [$s, $sb, $se];
	}

	foreach my $q (keys %match) {
		# get the known exons
		my @exon;
		my @f = split(/\|/, $q);
		my $chrom = $f[0];
		foreach my $estr (split(/,/, $f[3])) {
			my ($beg, $end) = split('-', $estr);
			push @exon, [$chrom, $beg, $end];
		}

		# get the alignments
		my @align;
		foreach my $hit (@{$match{$q}}) {
			next if overlaps(\@exon, $hit);
			print "@$hit similar to $q\n";
		}
	}
}

sub overlaps {
	my ($exons, $hit) = @_;
	my ($c1, $b1, $e1) = @$hit;
	foreach my $exon (@$exons) {
		my ($c2, $b2, $e2) = @$exon;
		return 0 if $c1 ne $c2;
		return 1 if $b2 <= $e1 and $e2 >= $b1;
	}
	return 0;
}

use warnings;
use strict;

my $prog;
my @time;
while (<>) {
	if (/BAKETIME %M %U %S %E" (\S+) (\S+)/) {
		if ($1 eq 'bwa') {$prog = "$1-$2"}
		} elsif ($1 eq 'STAR') {
			if ($2 eq "--runMode") {$prog = "star-index"}
			else                   {$prog = "star"}
		} else {$prog = $1}
	}
	if (/^BAKETIME (\d+) (\S+) (\S+)/) {
		push @time, {exe => $prog, mem => $1, cpu => $2 + $3}
	}
}

foreach my $t (@time) {print "$t->{exe}\t$t->{mem}\t$t->{cpu}\n"}

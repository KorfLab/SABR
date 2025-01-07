DIR="paper"
GOPTS="--double --noncanonical"
#PROGS="blat star" # for testing
PROGS="bbmp blat bow2 bwam gem3 gmap hst2 magi min2 pblt sege star subr top2"
#BOPTS="-dmts1" # for testing
BOPTS="-dmp9"

# fake genomes
mkdir -p $DIR
for i in $(seq 0 9);
do
	python3 src/genome-simulator.py fake$i --seed $i $GOPTS
	mv fake$i.fa fake$i.ftx $DIR
	./bakeoff $BOPTS $DIR/fake$i.f* $DIR/fake$i $PROGS > $DIR/fake$i.log 2>&1
done

# real genomes
./bakeoff $BOPTS data/at01.f* $DIR/at01 $PROGS > $DIR/at01.log 2>&1
./bakeoff $BOPTS data/ce01.f* $DIR/ce01 $PROGS > $DIR/ce01.log 2>&1
./bakeoff $BOPTS data/dm01.f* $DIR/dm01 $PROGS > $DIR/dm01.log 2>&1

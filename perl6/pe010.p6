my $sum = 0;
my $limit = 2000000;
my @primes = [0..$limit-1];
@primes[1] = 0;
loop (my $step = 2; $step < $limit; $step++) {
    unless @primes[$step] == 0 {
        loop (my $i = 2*$step; $i < $limit; $i+=$step) {
            @primes[$i] = 0;
        }
        $sum += $step;
    }
}
say $sum;
my $count = 1;
my $i = 3;
while $count < 10001 {
    $count += 1 if is-prime $i;
    $i+=2;
}
say $i-2;
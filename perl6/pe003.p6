my $num = 600851475143;
my $div = 2;
while $num != $div {
    if $num % $div == 0 {
        $num /= $div;
        $div--;
    }
    $div++;
}
say $div;
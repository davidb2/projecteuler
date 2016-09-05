my $ans = 0;
my $a = 1;
my $b = 1;
my $c = $a + $b;
while $c < 4000000 {
    $ans += $c if $c % 2 == 0;
    $a = $b;
    $c += $b;
    $b = $c - $b;
}
print $ans;
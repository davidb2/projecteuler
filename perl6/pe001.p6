my $ans = 0;
loop (my $i = 3; $i < 1000; $i++) {
    $ans += $i if $i % 3 == 0 or $i % 5 == 0;
}
print $ans;
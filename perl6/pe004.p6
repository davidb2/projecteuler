my $max = 0;
loop (my $x = 100; $x < 1000; $x++) {
    loop (my $y = 100; $y < 1000; $y++) {
        my $prod = $x * $y;
        if $prod == $prod.flip and $prod > $max {
            $max = $prod;
        }
    }
}
say $max;
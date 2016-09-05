loop (my $a = 1; $a < 1000; $a++) {
    loop (my $b = $a; $b < 1000; $b++) {
        my $c = sqrt($a**2+$b**2);
        if $c == floor($c) and $a+$b+$c == 1000 {
            say ($a*$b*$c);
            exit;
        }
    }
}
my @data = ([~] (slurp "../pe008.txt").lines)[0].split("", :skip-empty);
my $temp_prod = [*] @data[0..12];
my $max = $temp_prod;
loop (my $i = 13; $i < @data.elems; $i++) {
    $temp_prod /= @data[$i-13] != 0 ?? @data[$i-13] !! -1;
    $temp_prod *= @data[$i] != 0 ?? @data[$i] !! -1;
    $max = $temp_prod if $temp_prod > $max;
}
say $max;
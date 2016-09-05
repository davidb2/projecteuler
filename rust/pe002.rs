//pe2
use std::collections::HashMap;
fn main() {
	// initialize HashMap
    let mut fibs: HashMap<u32, u32> = HashMap::new();
	fibs.insert(0, 1);
	fibs.insert(1, 1);
	let mut n = 1;
	let mut sum = 0;
	while fib(n, &mut fibs) < 4000000 {
		sum += if fib(n, &mut fibs) % 2 == 0 {fib(n, &mut fibs)} else {0};
        n += 1;
	}
	println!("{}", sum);
}
fn fib(n: u32, fibs: &mut HashMap<u32, u32>) -> u32 {
    if !fibs.contains_key(&n) {
        let a = fib(n - 1, fibs);
        let b = fib(n - 2, fibs);
        fibs.insert(n, a + b);
    }
    *fibs.get(&n).unwrap()
}
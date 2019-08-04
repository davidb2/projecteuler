use std::collections::HashMap;

fn collatz(n: i64, cache: &mut HashMap<i64, i32>) -> i32 {
  if n == 1 {
    return 1;
  }

  if !cache.contains_key(&n) {
    if n % 2 == 0 {
      cache.insert(n, 1 + collatz(n / 2, cache));
    } else {
      cache.insert(n, 1 + collatz(3*n + 1, cache));
    }
  }
  return match cache.get(&n) {
    None => panic!("yo"),
    Some(&c) => c,
  };
}


fn main() {
  let mut cache = HashMap::new();
  for n in 1..10 {
    println!("{0} {1}", n, collatz(n, &mut cache));
  }
}
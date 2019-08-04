//pe1
fn main() {
  let ans =
    (1..1000)
    .filter(|x| x % 3 == 0 || x % 5 == 0)
    .collect::<Vec<u32>>()
    .iter()
    .fold(0, |x, y| x + y);
  println!("{}", ans);
}
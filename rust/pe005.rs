use std::cmp;

fn lcm(a:i32, b:i32) -> i32 {
    let mut min_mult:i32 = cmp::min(a, b);
    let min_num:i32 = cmp::min(a, b);
    let max_num:i32 = cmp::max(a, b);
    loop {
        if min_mult % max_num == 0 {
            return min_mult;
        } else {
            min_mult += min_num;
        }
    }
}
fn main() {
    println!("{}", (1..20).fold(1, |x, y| lcm(x, y)));
}
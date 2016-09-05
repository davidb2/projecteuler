fn main() {
    let a = (1..101).fold(0, |x, y| x+y);
    println!("{}",
        (a*a) - (1..101).map(|x| x*x).fold(0, |x, y| x+y)
    );
}
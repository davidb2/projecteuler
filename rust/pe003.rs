fn main() {
    let mut num:i64 = 600851475143;
    let mut divisor = 2;
    while num != divisor {
        if num % divisor == 0 {
            num /= divisor;
            divisor-=1;
        }
        divisor+=1;
    }
    println!("{}", divisor);
}
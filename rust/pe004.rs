fn is_palindrome(n: i32) -> bool {
    let str_num = n.to_string().into_bytes();
    for i in 0..3 {
        if str_num[i] != str_num[5-i] {
            return false;
        } 
    }
    true
}
fn main() {
    let mut max_pal:i32 = 0;
    let mut a:i32 = 999;
    let mut b:i32 = 999;
    while b > 900 {   
        while a > 112 {
            if is_palindrome(a*b) && a*b > max_pal {
                max_pal = a*b;
            } 
            a -= 1;
        }
        b -= 1;
        a = 999;
    }
    println!("{}", max_pal);
}
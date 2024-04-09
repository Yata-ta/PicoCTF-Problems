fn modular_exponentiation(c: u64, d: u64, n: u64) -> u64 {
    if n == 1 {
        return 0; // Invalid input, as the result is undefined when n is 1.
    }

    let mut result = 1;
    let mut base = c % n;

    let mut exponent = d;

    while exponent > 0 {
        if exponent % 2 == 1 {
            // If the least significant bit of exponent is 1, multiply result with base.
            result = (result * base) % n;
        }

        // Square the base and reduce modulo n.
        base = (base * base) % n;
        exponent /= 2;
    }

    result
}

fn main() {
    // Example usage:
    c: 861270243527190895777142537838333832920579264010533029282104230006461420086153423
    n: 1311097532562595991877980619849724606784164430105441327897358800116889057763413423
    e: 65537

    let result = modular_exponentiation(c, d, n);
    println!("m({}) = {} (mod {})", c, result, n);
}

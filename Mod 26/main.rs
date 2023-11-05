fn caesar_cipher(input: &str, shift: i32) -> String {
    let mut result = String::new();
    
    for c in input.chars() {
        let base = if c.is_ascii_lowercase() { 'a' as u32 } else if c.is_ascii_uppercase() { 'A' as u32 } else { result.push(c); continue };
        let shifted = (((c as u32 - base + shift as u32) % 26 + 26) % 26 + base) as u32;
        result.push(char::from_u32(shifted).unwrap());
    }
    
    result
}


fn main() {
    let phrase = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}";
    let n = 13;
    let decrypted = caesar_cipher(phrase, n);
    println!("Encrypted: {}", decrypted);
}


//solution
//picoCTF{next_time_I'll_try_2_rounds_of_rot13_ulYvpVag}
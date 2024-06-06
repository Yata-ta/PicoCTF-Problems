from random import randint
import sys


def generator(g, x, p):
    return pow(g, x) % p


def encrypt(plaintext, key):
    cipher = []
    for char in plaintext:
        cipher.append(((ord(char) * key*311)))
    return cipher

def decrypt(cipher, key):
    message = ""
    for character in cipher:
        try:
            decrypted_char = chr(character // (key * 311))
            message += decrypted_char
        except Exception as e:
            print(f"Error: {e}, Character: {character}, Key: {key}")
    return message



def is_prime(p):
    v = 0
    for i in range(2, p + 1):
        if p % i == 0:
            v = v + 1
    if v > 1:
        return False
    else:
        return True


def dynamic_xor_encrypt(plaintext, text_key):
    cipher_text = ""
    key_length = len(text_key)
    for i, char in enumerate(plaintext[::-1]):

        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    
    return cipher_text


def dynamic_xor_decrypt(cipher_text, text_key):
    decrypted_text = ""
    key_length = len(text_key)
    
    for i, char in enumerate(cipher_text):

        key_char = text_key[i % key_length]
        decrypted_char = chr(ord(char) ^ ord(key_char))
        decrypted_text += decrypted_char
    
    return decrypted_text[::-1]




def test(plain_text, text_key):
    p = 97
    g = 31
    if not is_prime(p) and not is_prime(g):
        print("Enter prime numbers")
        return
    a = randint(p-10, p)
    b = randint(g-10, g)
    a = 90
    b = 26

    print(f"a = {a}")
    print(f"b = {b}")
    u = generator(g, a, p)
    v = generator(g, b, p)
    key = generator(v, a, p)
    b_key = generator(u, b, p)
    shared_key = None
    if key == b_key:
        shared_key = key
    else:
        print("Invalid key")
        return
    print("Shared Key: {}".format(shared_key))
    print("U: {}".format(u))
    print("V: {}".format(v))
    semi_cipher = dynamic_xor_encrypt(plain_text, text_key)
    print("Semi Cipher: {}".format(semi_cipher))
    cipher = encrypt(semi_cipher, shared_key)
    print(f'cipher is: {cipher}')  
    

    semi_cipher = decrypt(cipher, shared_key)
    print(f'Semi-Cipher: {semi_cipher}')

    message = dynamic_xor_decrypt(semi_cipher, text_key)

    print("Decrypted Message: ")
    print(message)



if __name__ == "__main__":
    message = sys.argv[1]
    test(message, "trudeau")

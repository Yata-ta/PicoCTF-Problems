import base64
decoded_data = base64.b64decode("YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclh6ZzVNR3N5TXpjNWZRPT0nCg==")

print("decoded text is ")
print(decoded_data)


# Remove initial b, quotes, and newline
decoded_string = decoded_data.decode('utf-8').strip("b'\\n")

# Decode Base64
decoded_data = base64.b64decode(decoded_string)

# Convert bytes to string
decoded_text = decoded_data.decode('utf-8')

print("Decoded text is:")
print(decoded_text)


def caesar_cipher_decode(text, shift):
    decoded_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                decoded_text += chr((ord(char) - shift - 97) % 26 + 97)
            elif char.isupper():
                decoded_text += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            decoded_text += char
    return decoded_text

# Try all 27 shifts and print decoded texts
print("Decoded texts using Caesar cipher:")
for shift in range(27):
    decoded_caesar = caesar_cipher_decode(decoded_text, shift)
    print(f"Shift {shift}: {decoded_caesar}")

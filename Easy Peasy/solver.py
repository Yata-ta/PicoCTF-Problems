import pwn

KEY_LEN = 50000
MAX_CHUNK = 1000

# Connect to the service
r = pwn.remote("mercury.picoctf.net", 20266)

# Receive the encrypted flag
r.recvuntil("This is the encrypted flag!\n")
flag = r.recvlineS(keepends=False)
pwn.log.info(f"Encrypted Flag: {flag}")
bin_flag = pwn.unhex(flag)
print("Bin Flag: {}".format(bin_flag))


# Calculate how many bytes we need to send to cause wrap-around
counter = KEY_LEN - len(bin_flag)

# Send arbitrary data to cause the key to wrap around and repeat
with pwn.log.progress('Causing wrap-around') as p:
    while counter > 0:
        p.status(f"{counter} bytes left")
        chunk_size = min(MAX_CHUNK, counter)
        r.sendlineafter("What data would you like to encrypt? ", "a" * chunk_size)
        counter -= chunk_size

# Send the encrypted flag again to get the same key used to encrypt it
r.sendlineafter("What data would you like to encrypt? ", bin_flag)

# Receive the re-encrypted flag and XOR it with the obtained key to decrypt the flag
r.recvlineS()
decrypted_flag = pwn.unhex(r.recvlineS())
pwn.log.success(f"Decrypted Flag: {decrypted_flag}")

# Close the connection
r.close()

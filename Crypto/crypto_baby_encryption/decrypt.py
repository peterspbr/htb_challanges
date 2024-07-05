def decryption(encrypted_msg):
    decrypted_msg = []
    mod_inverse = pow(123, -1, 256)  # Modular inverse of 123 modulo 256
    for char in encrypted_msg:
        decrypted_char = (mod_inverse * (char - 18)) % 256
        decrypted_msg.append(decrypted_char)
    return bytes(decrypted_msg)

with open('./msg.enc', 'r') as f:
    encrypted_hex = f.read()

encrypted_bytes = bytes.fromhex(encrypted_hex)

decrypted_msg = decryption(encrypted_bytes)

print(decrypted_msg.decode())

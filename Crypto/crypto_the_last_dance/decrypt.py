'''
The reuse of the key and nonce for encrypting multiple pieces of data is the main vulnerability exploited in this challenge.
ChaCha20, like other stream ciphers, generates a keystream based on the key and nonce provided. The encryption is performed by XORing the plaintext with this keystream.
If the key and nonce are reused, the same keystream is generated, which can lead to security breaches.

Solution Approach

Extract the KeyStream:
Since the known plaintext and ciphertext are available, we can derive the keystream used during encryption by XORing them together.
The equation for this step is: Keystream = Known Plaintext ⊕ Ciphertext

Decrypt the flag:
With the keystream known, decrypting the flag is straightforward.
We apply the XOR operation between the encrypted flag and the derived keystream: Decrypted Flag = Encrypted Flag ⊕ Keystream

Reference: https://medium.com/@krishgera1/the-last-dance-hackthebox-writeup-ab0ffda6264f
'''

def hex_xor(hex1, hex2):
    min_length = min(len(hex1), len(hex2))
    bytes1 = bytes.fromhex(hex1[:min_length])
    bytes2 = bytes.fromhex(hex2[:min_length])
    xor_result = ''.join(f"{b1 ^ b2:02x}" for b1, b2 in zip(bytes1, bytes2))
    return xor_result

if __name__ == "__main__":
    message = b"Our counter agencies have intercepted your messages and a lot "
    message += b"of your agent's identities have been exposed. In a matter of "
    message += b"days all of them will be captured"

    known_text = message.hex()
    #print(known_text)

    encrypted_message = "7aa34395a258f5893e3db1822139b8c1f04cfab9d757b9b9cca57e1df33d093f07c7f06e06bb6293676f9060a838ea138b6bc9f20b08afeb73120506e2ce7b9b9dcd9e4a421584cfaba2481132dfbdf4216e98e3facec9ba199ca3a97641e9ca9782868d0222a1d7c0d3119b867edaf2e72e2a6f7d344df39a14edc39cb6f960944ddac2aaef324827c36cba67dcb76b22119b43881a3f1262752990"
    encrypted_messagee = encrypted_message[:len(known_text)]
    #print(encrypted_messagee)

    keystream = hex_xor(known_text, encrypted_messagee)
    #print(keystream)

    encrypted_flag = "7d8273ceb459e4d4386df4e32e1aecc1aa7aaafda50cb982f6c62623cf6b29693d86b15457aa76ac7e2eef6cf814ae3a8d39c7"
    decrypted_flag = hex_xor(keystream, encrypted_flag)
    #print(decrypted_flag)

    decoded_flag = bytes.fromhex(decrypted_flag).decode('utf-8')
    print(decoded_flag)
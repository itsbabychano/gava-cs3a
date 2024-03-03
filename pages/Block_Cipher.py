import streamlit as st

def pad(data, block_size):  
    # CMS (Cryptographic Message Syntax) padding with the same value as padding bytes.
    padding_length = block_size - len(data) % block_size
    padding = bytes([padding_length] * padding_length) 
    return data + padding 

def unpad(data):
    padding_length = data[-1]
    assert padding_length > 0 
    message, padding = data[:-padding_length], data[-padding_length:]
    assert all(p == padding_length for p in padding)
    return message  

def xor_encrypt_block(plaintext_block, key):
    encrypted_block = b''
    for i in range(len(plaintext_block)):
        encrypted_block += bytes([plaintext_block[i] ^ key[i % len(key)]])
    return encrypted_block  

def xor_decrypt_block(ciphertext_block, key):
    return xor_encrypt_block(ciphertext_block, key) 

def xor_encrypt(plaintext, key, block_size):
    encrypted_data = b''
    padded_plaintext = pad(plaintext, block_size)
    print("Encrypted blocks")
    for x, i in enumerate(range(0, len(padded_plaintext), block_size)):
        plaintext_block = padded_plaintext[i:i+block_size]
        encrypted_block = xor_encrypt_block(plaintext_block, key)
        print(f"Plain  block[{x}]: {plaintext_block.hex()} : {plaintext_block}")
        print(f"Cipher block[{x}]: {encrypted_block.hex()} : {encrypted_block}")
        encrypted_data += encrypted_block
    return encrypted_data 

def xor_decrypt(ciphertext, key, block_size):
    decrypted_data = b''
    print("Decrypted blocks")
    for x, i in enumerate(range(0, len(ciphertext), block_size)):
        ciphertext_block = ciphertext[i:i+block_size]
        decrypted_block = xor_decrypt_block(ciphertext_block, key)
        print(f"block[{x}]: {decrypted_block.hex()}: {decrypted_block}")
        decrypted_data += decrypted_block
    unpadded_decrypted_data = unpad(decrypted_data)
    return unpadded_decrypted_data  

# Streamlit App
st.title("XOR Encryption/Decryption") 

plaintext = st.text_input("Enter plaintext:")
key = st.text_input("Enter key:")
block_size = st.number_input("Enter block size (8, 16, 32, 64, 128):", min_value=8, max_value=128, value=16, step=8)

if st.button("Encrypt"):
    if block_size in [8, 16, 32, 64, 128]:
        key = pad(key.encode(), block_size)
        ciphertext = xor_encrypt(plaintext.encode(), key, block_size)
        st.write("**Encrypted Data (Hexadecimal):**")
        st.code(ciphertext.hex()) 

        decrypted_data = xor_decrypt(ciphertext, key, block_size)
        st.write("**Decrypted Data (Hexadecimal):**")
        st.code(decrypted_data.hex())
        st.write("**Decrypted Data:**") 
        st.write(decrypted_data)
    else:
        st.error("Block size must be one of 8, 16, 32, 64, or 128 bytes")

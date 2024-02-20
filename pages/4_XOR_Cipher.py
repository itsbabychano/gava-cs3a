import streamlit as st

st.header("XOR Cipher")

plaintext = bytes(st.text_area("Plain Text:").encode())

key = bytes(st.text_input("Key:").encode())

def xor_encrypt(plaintext, key):
    """Encrypts plaintext using XOR cipher with the given key, st.writeing bits involved."""

    ciphertext = bytearray()
    for i in range(len(plaintext)):
        input_text_byte = plaintext[i]
        key_byte =  key[i % len(key)]
        encrypted_byte = input_text_byte ^ key_byte
        ciphertext.append(encrypted_byte)
        st.write(f"plaintext byte: {format(input_text_byte, '08b')} = {chr(input_text_byte)}")
        st.write(f"Key byte:       {format(key_byte, '08b')} = {chr(key_byte)}")
        st.write(f"XOR result:     {format(encrypted_byte, '08b')} = {chr(encrypted_byte)}")
        
        st.write("--------------------")
    return ciphertext


def xor_decrypt(ciphertext, key):
    """Decrypts ciphertext using XOR cipher with the given key."""
    return xor_encrypt(ciphertext, key)   # XOR decryption is the same as encryption



if st.button("Submit"):
    if plaintext.decode() == key.decode():
        print("plaintext should not be equal to the key")
    
    elif len(key.decode()) > len(plaintext.decode()):
        print("plaintext length should be equal or greater than the length of key")
    else:
        encrypted_text = xor_encrypt(plaintext, key)
        print("Ciphertext:", encrypted_text.decode())
        decrypted_text = xor_decrypt(encrypted_text, key)
        print("Decrypted:", plaintext.decode())
        st.write(plaintext)


import streamlit as st

st.header("XOR Cipher")

# Layout and Explanatory text
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Encryption**")
    plaintext = bytes(st.text_area("Plain Text:", help="Enter the text you want to encrypt").encode())
    key = bytes(st.text_input("Key:", help="Enter a key for the cipher").encode())

with col2:
    st.markdown("**Decryption**")
    ciphertext = bytes(st.text_area("Ciphertext:", help="Enter the ciphertext to decrypt").encode())
    key2 = bytes(st.text_input("Key (same as for encryption):").encode())  # Renamed from 'key'

# Button and Output
if st.button("Submit"):
    if plaintext.decode() == key.decode():
        st.error("Plaintext should not be equal to the key")
    elif len(key.decode()) > len(plaintext.decode()):
        st.error("Plaintext length should be equal or greater than the length of key")
    else:
        if plaintext and key and not ciphertext:  # Assuming encryption 
            st.markdown("**Encryption Results**")
            encrypted_text = xor_encrypt(plaintext, key)
            st.write("Ciphertext:", encrypted_text.decode())
        elif ciphertext and key2 and not plaintext:  # Assuming decryption
            st.markdown("**Decryption Results**")
            decrypted_text = xor_decrypt(ciphertext, key2)
            st.write("Decrypted:", decrypted_text.decode())

# Your xor_encrypt and xor_decrypt definitions (Place these below) 
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


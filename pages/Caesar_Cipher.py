import streamlit as st

def encrypt_decrypt(text, shift_keys, ifdecrypt):
    result = ""
    if len(shift_keys) <= 1 or len(shift_keys) > len(text):
        raise ValueError("Invalid shift key length")
    for i, char in enumerate(text):
        shift_key = shift_keys[i % len(shift_keys)]
        if 32 <= ord(char) <= 125:
            new_ascii = ord(char) + shift_key if not ifdecrypt else ord(char) - shift_key
            while new_ascii > 125:
                new_ascii -= 94
            while new_ascii < 32:
                new_ascii += 94
            result += chr(new_ascii)
        else:
            result += char
    return result

st.title("Caesar Cipher Encryptor/Decryptor")
text = st.text_input("Enter your text:", "Hello world") 
shift_keys_str = st.text_input("Enter shift keys (space-separated):", "2 4 3 22 -5") 
shift_keys = [int(key) for key in shift_keys_str.split()]

if st.button("Encrypt"):
    try:
        encrypted_text = encrypt_decrypt(text, shift_keys, False)
        st.success("Encrypted Text:")
        st.code(encrypted_text)  
    except ValueError as e:
        st.error(e) 

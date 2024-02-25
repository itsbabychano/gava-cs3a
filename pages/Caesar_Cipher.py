import streamlit as st

def encrypt_decrypt(text, shift_keys, ifdecrypt):
    """
    Encrypts a text using Caesar Cipher with a list of shift keys.

    Args:
        text: The text to encrypt.
        shift_keys: A list of integers representing the shift values for each character.
        ifdecrypt: Flag indicating whether to encrypt or decrypt.

    Returns:
        A string containing the encrypted text if encrypt and plain text if decrypt.
    """
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


# Streamlit app
st.title("Caesar Cipher Encryptor/Decryptor")

text = st.text_input("Enter your text:")
shift_keys_str = st.text_input("Enter shift keys (space-separated):")
shift_keys = [int(key) for key in shift_keys_str.split()]

if st.button("Encrypt"):
    try:
        encrypted_text = encrypt_decrypt(text, shift_keys, False)
        st.success("Encrypted Text:")
        st.code(encrypted_text)  # Display as code block
    except ValueError as e:
        st.error(e)

if st.button("Decrypt"):
    try:
        decrypted_text = encrypt_decrypt(text, shift_keys, True)
        st.success("Decrypted Text:")
        st.code(decrypted_text)
    except ValueError as e:
        st.error(e)

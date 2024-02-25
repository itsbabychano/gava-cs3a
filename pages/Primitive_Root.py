import streamlit as st

def prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 ==0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def check_primitive(g, p):
    """Finds primitive roots of a prime number."""
    primitive_roots = []
    for i in range(1, p):
        temp = set()
        output = ''
        for j in range(1, p):
            res = pow(i, j, p)
            output += f"{i}^{j} mod {p} = {res}"
            if j < p - 1:
                output += ", "
            temp.add(res)
            if res == 1:
                break
        if len(temp) == p - 1:
            primitive_roots.append(i)
            output += f" ==> {i} is primitive root of {p}, "
        st.write(output)  # Display output in Streamlit
    return g in primitive_roots, primitive_roots


# Streamlit app
st.title("Primitive Root Checker")

q = st.number_input("Enter a number (q):", min_value=2)
g = st.number_input("Enter a potential primitive root (g):", min_value=1)

if st.button("Check"):
    if prime(q):
        is_primitive_roots, primitive_roots = check_primitive(g, q)
        if is_primitive_roots:
            st.success(f"{g} is a primitive root of {q}. List of primitive roots: {primitive_roots}")
        else:
            st.warning(f"{g} is NOT a primitive root of {q}. List of primitive roots: {primitive_roots}")
    else:
        st.error(f"{q} is not a prime number!")

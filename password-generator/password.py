import streamlit as st
import random 
import string

def generate_password(length , use_digits , use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits #adds numbers (0-9) if selected

    if use_special:
        characters += string.punctuation #addition of special characters (! , @ , # , $ , % , ^ , & , * ,)
    
    return ''.join(random.choice(characters) for _ in range (length))


st.title ("Password Generator")

length = st.slider("Select password length" , min_value=4 , max_value=30)

use_digits = st.checkbox("Include digits")

use_special = st.checkbox("Include special characters")

if st.button("Generate Password"):
    password = generate_password(length , use_digits , use_special)
    st.write(f"Generated Password: `{password}`")

st.write("________________________")

st.write ("Builded with ❤️ by [SAUDALI](github.com/saudali195)")

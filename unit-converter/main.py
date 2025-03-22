import streamlit as st

def convert_units(value , unit_from , unit_to):

    conversions = {
        "meter_kilometer" : 0.001, # 1 meter  = 0.001kilometer
        "kilometer_meter" : 1000, # 1 kilometer = 1000 meters
        "gram_kilogram" : 0.001, # 1 gram = 0.001 kilogram
        "kilogram_gram" : 1000, # 1 kilogram = 1000 grams
    }

    key = f"{unit_from}_{unit_to}" # generate a key based on the input and output units

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not Supported"
    
st.title("unit Converter")

value = st.number_input("Enter the value to convert")

unit_from = st.selectbox("Convert from:", ["meter" , "kilometer" , "gram" , "kilogram"])

unit_to = st.selectbox("Convert to:", ["meter" , "kilometer" , "gram" , "kilogram"])

if st.button("Convert"):
    result = convert_units(value , unit_from , unit_to)
    st.write(f"Converted Value: {result}")
    
    
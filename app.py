import streamlit as st
from PIL import Image

# Title and Header
st.set_page_config(page_title="Unit Converter", page_icon="📏", layout="wide")
st.title("✨ Unit Converter ✨")

# Custom CSS for dropdown hover effect
st.markdown("""
    <style>
        .main {
            background-color: #f0f8ff;
            padding: 20px;
            border-radius: 15px;
        }
        h1 {
            color: #4B0082;
            text-align: center;
        }
        h3 {
            color: #6A5ACD;
        }
        .stButton > button {
            background-color: #4B0082;
            color: white;
            border-radius: 10px;
            font-size: 16px;
            padding: 10px 20px;
        }
        .stButton > button:hover {
            background-color: #6A5ACD;
        }
        /* Add pointer cursor to dropdowns */
        .stSelectbox div[data-baseweb="select"] > div {
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar for additional information
st.sidebar.image(Image.open("converter_logo.png"), use_container_width=True)
st.sidebar.markdown("### Welcome to the Unit Converter!")
st.sidebar.info("""
    This app allows you to convert between various units of measurement. 
    Choose a category, select the units, and input your value to get started!
""")

# Conversion Categories
categories = {
    "Length": {"meters": 1, "kilometers": 1000, "miles": 1609.34, "feet": 0.3048},
    "Weight": {"grams": 1, "kilograms": 1000, "pounds": 453.592, "ounces": 28.3495},
    "Temperature": {"Celsius": lambda x: x, "Fahrenheit": lambda x: (x - 32) * 5 / 9, "Kelvin": lambda x: x - 273.15}
}

# Select Category
st.subheader("Select Conversion Category")
category = st.selectbox("Choose a category:", list(categories.keys()))

# Select Units
st.subheader("Select Units")
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From:", list(categories[category].keys()))
with col2:
    to_unit = st.selectbox("To:", list(categories[category].keys()))

# Input Value
st.subheader("Enter Value")
value = st.number_input("Input the value to convert:", min_value=0.0, step=0.1)

# Perform Conversion
if st.button("Convert"):
    if category == "Temperature":
        # Temperature conversion logic
        try:
            converted_value = categories[category][to_unit](categories[category][from_unit](value))
            st.success(f"{value} {from_unit} = {converted_value:.2f} {to_unit}")
        except Exception as e:
            st.error("An error occurred during temperature conversion.")
    else:
        # General unit conversion logic
        base_value = value * categories[category][from_unit]
        converted_value = base_value / categories[category][to_unit]
        st.success(f"{value} {from_unit} = {converted_value:.2f} {to_unit}")

# Footer
st.markdown("---")
st.markdown("Created with ❤️ by Syed Muhammad Shan-e-Ali")
import streamlit as st
import pandas as pd
import joblib

# Load model and features
model = joblib.load("laptop_price_model.pkl")
features = joblib.load("features.pkl")

st.title("💻 Laptop Price Prediction")

# User Inputs
brand = st.selectbox("Brand", ["HP","Dell","Lenovo","Asus","Acer","MSI","Apple"])

spec_rating = st.number_input("Specification Rating", min_value=0)

ram = st.number_input("RAM (GB)", min_value=2)

rom = st.number_input("Storage (GB)", min_value=128)

display_size = st.number_input("Display Size", value=15.6)

resolution_width = st.number_input("Resolution Width", value=1920)

resolution_height = st.number_input("Resolution Height", value=1080)

warranty = st.number_input("Warranty (Years)", value=1)

processor = st.selectbox(
    "Processor",
    ["Intel Core i3","Intel Core i5","Intel Core i7","AMD Ryzen 5","AMD Ryzen 7"]
)

cpu = st.selectbox(
    "CPU",
    ["Intel","AMD","Apple"]
)

ram_type = st.selectbox(
    "RAM Type",
    ["DDR4","DDR5","LPDDR4","LPDDR5"]
)

rom_type = st.selectbox(
    "Storage Type",
    ["SSD","HDD"]
)

gpu = st.selectbox(
    "GPU",
    ["Integrated","NVIDIA","AMD"]
)

os = st.selectbox(
    "Operating System",
    ["Windows","Mac","Linux"]
)

if st.button("Predict Price"):

    data = {
        "spec_rating":[spec_rating],
        "Ram":[ram],
        "ROM":[rom],
        "display_size":[display_size],
        "resolution_width":[resolution_width],
        "resolution_height":[resolution_height],
        "warranty":[warranty],
        "brand":[brand],
        "processor":[processor],
        "CPU":[cpu],
        "Ram_type":[ram_type],
        "ROM_type":[rom_type],
        "GPU":[gpu],
        "OS":[os]
    }

    df = pd.DataFrame(data)

    # One-hot encode
    df = pd.get_dummies(df)

    # Match training columns
    df = df.reindex(columns=features, fill_value=0)

    prediction = model.predict(df)

    st.success(f"Estimated Laptop Price: ₹{prediction[0]:,.0f}")
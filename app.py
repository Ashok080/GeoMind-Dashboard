import streamlit as st
import numpy as np
import rasterio
import matplotlib.pyplot as plt

st.set_page_config(page_title="GeoMind-AI", layout="wide")
st.title("🛰️ GeoMind-AI: Satellite-based Mineral Detection")
st.markdown("Upload a `.hgt` SRTM file to view elevation and detect mock mineral zones.")

uploaded_file = st.file_uploader("📂 Upload SRTM .hgt file", type=["hgt"])

if uploaded_file is not None:
    with open("temp_dem.hgt", "wb") as f:
        f.write(uploaded_file.read())

    try:
        with rasterio.open("temp_dem.hgt") as src:
            elevation = src.read(1)

        st.success("✅ DEM loaded successfully!")
        st.write("**Shape:**", elevation.shape)

        st.subheader("🌄 Elevation Map")
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.imshow(elevation, cmap='terrain')
        ax.set_title("Digital Elevation Map")
        ax.axis('off')
        st.pyplot(fig)

        st.subheader("🧠 Mineral Prediction (Mock)")
        mask = (elevation > 500) & (elevation < 1500)
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        ax2.imshow(mask, cmap='hot', alpha=0.6)
        ax2.set_title("Predicted Mineral Zones")
        ax2.axis('off')
        st.pyplot(fig2)

    except Exception as e:
        st.error(f"Error reading DEM: {e}")
else:
    st.info("📎 Please upload a `.hgt` DEM file to get started.")


---

import streamlit as st
from PIL import Image
import numpy as np

st.set_page_config(page_title="AI Mammogram Analysis", page_icon="🎗️", layout="centered")

# ===== دالة إزالة الخلفية البيضاء من الصورة =====
def remove_white_background(image_path, threshold=240):
    img = Image.open(image_path).convert("RGBA")
    data = np.array(img)
    r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
    white_mask = (r > threshold) & (g > threshold) & (b > threshold)
    data[:,:,3] = np.where(white_mask, 0, a)
    return Image.fromarray(data)

st.markdown("""
<style>
.stApp {
    background-color: #FDF8FB;
}
.main-title {
    color: #C2185B;
    text-align: center;
    font-family: 'Arial', sans-serif;
    font-weight: bold;
    font-size: 30px;
    margin-bottom: 20px;
}
.sub-title {
    color: #AD1457;
    text-align: left;
    font-family: 'Arial', sans-serif;
    font-weight: bold;
    margin-bottom: 20px;
}
.quote-box {
    background-color: #E91E8C;
    color: #FFFFFF !important;
    padding: 12px;
    border-radius: 15px;
    text-align: center;
    font-style: italic;
    margin-top: 25px;
    font-size: 14px;
    font-weight: 500;
}
div.stButton > button {
    background-color: #E91E8C !important;
    color: #FFFFFF !important;
    border-radius: 20px;
    border: none;
    padding: 8px 30px;
    font-weight: bold;
    width: 100%;
    box-shadow: 0px 4px 6px rgba(233, 30, 140, 0.3);
}
div.stButton > button:hover {
    background-color: #AD1457 !important;
    color: #FFFFFF !important;
}
div[data-testid="stTextInput"] input {
    border: 1.5px solid #F48FB1 !important;
    border-radius: 10px !important;
    background-color: #FFF0F5 !important;
    color: #880E4F !important;
}
div[data-testid="stTextInput"] input:focus {
    border-color: #E91E8C !important;
    box-shadow: 0 0 0 2px rgba(233,30,140,0.15) !important;
}
div[data-testid="stRadio"] label {
    color: #AD1457 !important;
    font-weight: bold;
}
hr {
    border-color: #F48FB1 !important;
}
div[data-testid="stTextInput"] label,
div[data-testid="stRadio"] > label {
    color: #C2185B !important;
    font-weight: bold !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>AI-Powered Mammogram Analysis for Early Breast Cancer Detection</h1>", unsafe_allow_html=True)
st.write("---")
st.markdown("<h3 class='sub-title'>Your health matters ❤️</h3>", unsafe_allow_html=True)

col1, col2 = st.columns([1.2, 1])

with col1:
    patient_name = st.text_input("Patient Name", placeholder="Enter patient name")
    patient_age = st.text_input("Patient Age", placeholder="Enter age")
    phone_number = st.text_input("Phone Number", placeholder="Enter phone number")
    medical_history = st.radio("Medical History", ["No", "Yes"], index=0)

with col2:
    try:
        # ✅ هنا يصير إزالة الخلفية فعلياً
        clean_img = remove_white_background("my2.jpg", threshold=240)
        st.image(clean_img, width=270)
    except Exception as e:
        st.warning(f"تعذر تحميل الصورة: {e}")

    st.markdown("<div class='quote-box'>\"Like butterflies we flourish when we feel safe\"</div>", unsafe_allow_html=True)

st.write("\n\n")

col_btn1, col_btn2, col_btn3, col_btn4 = st.columns([1, 2, 2, 1])

with col_btn2:
    if st.button("« Back"):
        st.info("Back button clicked")

with col_btn3:
    if st.button("Next »"):
        st.success("Proceeding to the next step...")

import streamlit as st

st.set_page_config(page_title="AI Mammogram Analysis", page_icon="🎗️", layout="centered")

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

/* إزالة الخلفية من الصورة بشكل كامل */
.transparent-img img {
    mix-blend-mode: multiply;
    background-color: transparent !important;
    background: none !important;
}
.transparent-img [data-testid="stImage"] {
    background-color: transparent !important;
    background: none !important;
}
.transparent-img [data-testid="stImage"] > img {
    background-color: transparent !important;
    mix-blend-mode: multiply;
    filter: contrast(1.05);
}

/* تلوين حقول الإدخال بالوردي */
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

/* تلوين الـ Radio بالوردي */
div[data-testid="stRadio"] label {
    color: #AD1457 !important;
    font-weight: bold;
}
div[data-testid="stRadio"] input[type="radio"]:checked + div {
    background-color: #E91E8C !important;
}

/* تلوين الفاصل */
hr {
    border-color: #F48FB1 !important;
}

/* label فوق حقول الإدخال */
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
    st.markdown('<div class="transparent-img">', unsafe_allow_html=True)
    try:
        st.image("my2.jpg", width=270)
    except Exception as e:
        st.warning("Image 'my2.jpg' not found.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<div class='quote-box'>\"Like butterflies we flourish when we feel safe\"</div>", unsafe_allow_html=True)

st.write("\n\n")

col_btn1, col_btn2, col_btn3, col_btn4 = st.columns([1, 2, 2, 1])

with col_btn2:
    if st.button("« Back"):
        st.info("Back button clicked")

with col_btn3:
    if st.button("Next »"):
        st.success("Proceeding to the next step...")

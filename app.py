import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="AI Mammogram Analysis", page_icon="🎗️", layout="centered")

# 2. تخصيص الألوان والتنسيقات
st.markdown("""
<style>
.stApp {
    background-color: #FDF8FB;
}
.main-title {
    color: #A3488E;
    text-align: center;
    font-family: 'Arial', sans-serif;
    font-weight: bold;
    font-size: 30px;
    margin-bottom: 20px;
}
.sub-title {
    color: #7A306C;
    text-align: left;
    font-family: 'Arial', sans-serif;
    font-weight: bold;
    margin-bottom: 20px;
}
.quote-box {
    background-color: #A3488E;
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
    background-color: #B35B9D !important;
    color: #FFFFFF !important;
    border-radius: 20px;
    border: none;
    padding: 8px 30px;
    font-weight: bold;
    width: 100%;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}
div.stButton > button:hover {
    background-color: #7A306C !important;
    color: #FFFFFF !important;
}

/* إزالة الخلفية البيضاء من الصورة بشكل كامل */
.transparent-img img {
    mix-blend-mode: multiply;
    background-color: transparent !important;
    background: none !important;
}

/* إزالة أي خلفية من الحاوية المحيطة بالصورة في Streamlit */
.transparent-img [data-testid="stImage"] {
    background-color: transparent !important;
    background: none !important;
}

.transparent-img [data-testid="stImage"] > img {
    background-color: transparent !important;
    mix-blend-mode: multiply;
    filter: contrast(1.05);
}
</style>
""", unsafe_allow_html=True)

# 3. عرض العنوان الرئيسي
st.markdown("<h1 class='main-title'>AI-Powered Mammogram Analysis for Early Breast Cancer Detection</h1>", unsafe_allow_html=True)
st.write("---")

# 4. عرض العنوان الفرعي
st.markdown("<h3 class='sub-title'>Your health matters ❤️</h3>", unsafe_allow_html=True)

# 5. تقسيم الواجهة إلى عمودين
col1, col2 = st.columns([1.2, 1])

with col1:
    patient_name = st.text_input("Patient Name", placeholder="Enter patient name")
    patient_age = st.text_input("Patient Age", placeholder="Enter age")
    phone_number = st.text_input("Phone Number", placeholder="Enter phone number")
    medical_history = st.radio("Medical History", ["No", "Yes"], index=0)

with col2:
    # ✅ التعديل: إزالة الخلفية وتكبير الصورة من 220 إلى 270
    st.markdown('<div class="transparent-img">', unsafe_allow_html=True)
    try:
        st.image("my2.jpg", width=270)  # ← تم التكبير هنا
    except Exception as e:
        st.warning("Image 'my2.jpg' not found.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<div class='quote-box'>\"Like butterflies we flourish when we feel safe\"</div>", unsafe_allow_html=True)

st.write("\n\n")

# 6. أزرار التحكم
col_btn1, col_btn2, col_btn3, col_btn4 = st.columns([1, 2, 2, 1])

with col_btn2:
    if st.button("« Back"):
        st.info("Back button clicked")

with col_btn3:
    if st.button("Next »"):
        st.success("Proceeding to the next step...")

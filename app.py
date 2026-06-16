import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="AI Mammogram Analysis", page_icon="🎗️", layout="centered")

# 2. التنسيق المتقدم والمثالي بالألوان المطلوبة
st.markdown("""
    <style>
    /* خلفية التطبيق العامة مريحة ومتناسقة مع الوردي */
    .stApp {
        background-color: #FDF9FB;
    }
    
    /* اسم المشروع باللون الوردي الغامق والخط العريض */
    .main-title {
        color: #7A306C;
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 800;
        font-size: 32px;
        margin-bottom: 25px;
        line-height: 1.3;
    }
    
    /* العنوان الفرعي بالوردي */
    .sub-title {
        color: #A3488E;
        text-align: left;
        font-family: 'Segoe UI', sans-serif;
        font-weight: 700;
        margin-bottom: 20px;
    }
    
    /* صندوق الجملة: خلفية وردية تماماً والكتابة بيضاء */
    .quote-box {
        background-color: #A3488E;
        color: #FFFFFF !important;
        padding: 14px;
        border-radius: 12px;
        text-align: center;
        font-style: italic;
        margin-top: 20px;
        font-size: 13.5px;
        font-weight: bold;
        box-shadow: 0px 4px 10px rgba(163, 72, 142, 0.2);
    }
    
    /* الأزرار في الأسفل: خلفية وردية ملونة ونصوص بيضاء ناصعة */
    div.stButton > button {
        background-color: #B35B9D !important;
        color: #FFFFFF !important;
        border-radius: 25px;
        border: none;
        padding: 10px 35px;
        font-weight: bold;
        font-size: 15px;
        width: 100%;
        box-shadow: 0px 4px 8px rgba(179, 91, 157, 0.3);
        transition: all 0.3s ease;
    }
    
    /* تأثير أنيق عند تمرير الماوس فوق الأزرار */
    div.stButton > button:hover {
        background-color: #7A306C !important;
        color: #FFFFFF !important;
        transform: translateY(-2px);
        box-shadow: 0px 6px 12px rgba(122, 48, 108, 0.4);
    }
    
    /* جعل حقول الإدخال تبدو أنظف وأجمل */
    .stTextInput > div > div > input {
        border-radius: 8px;
        border: 1px solid #E0D0DC;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. عرض العنوان الرئيسي بالوردي
st.markdown("<h1 class='main-title'>AI-Powered Mammogram Analysis for Early Breast Cancer Detection</h1>", unsafe_allow_html=True)
st.write("---")

# 4. عرض العنوان الفرعي
st.markdown("<h3 class='sub-title'>Your health matters ❤</h3>", unsafe_allow_html=True)

# 5. تقسيم الواجهة إلى عمودين
col1, col2 = st.columns([1.2, 1])

with col1:
    # حقول إدخال البيانات
    patient_name = st.text_input("Patient Name", placeholder="Enter patient name")
    patient_age = st.text_input("Patient Age", placeholder="Enter age")
    phone_number = st.text_input("Phone Number", placeholder="Enter phone number")
    
    # اختيار التاريخ الطبي
    medical_history = st.radio("Medical History", ["No", "Yes"], index=0)

with col2:
    # عرض صورة احترافية بشريط وردي وفراشة بخلفية شفافة 100% لتندمج مع اللون الوردي للموقع
    st.image("https://i.ibb.co/VWVg0YtM/pink-ribbon-butterfly.png", width=220)
    
    # العبارة التشجيعية بخلفية وردية ونص أبيض
    st.markdown("<div class='quote-box'>\"Like butterflies we flourish when we feel safe\"</div>", unsafe_allow_html=True)

st.write("\n\n") 

# 6. أزرار التحكم في أسفل الصفحة
col_btn1, col_btn2, col_btn3, col_btn4 = st.columns([1, 2, 2, 1])

with col_btn2:
    if st.button("« Back"):
        st.info("Back button clicked")

with col_btn3:
    if st.button("Next »"):
        st.success("Proceeding to the next step...")

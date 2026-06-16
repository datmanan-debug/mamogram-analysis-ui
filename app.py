import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="AI Mammogram Analysis", page_icon="🎗️", layout="centered")

# 2. تخصيص الألوان والتنسيقات بالكامل بناءً على طلبك
st.markdown("""
    <style>
    /* جعل خلفية التطبيق متناسقة */
    .stApp {
        background-color: #FDF8FB;
    }
    
    /* اسم المشروع باللون الوردي الداكن المميز */
    .main-title {
        color: #A3488E;
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-weight: bold;
        font-size: 30px;
        margin-bottom: 20px;
    }
    
    /* العنوان الفرعي بالوردي */
    .sub-title {
        color: #7A306C;
        text-align: left;
        font-family: 'Arial', sans-serif;
        font-weight: bold;
        margin-bottom: 20px;
    }
    
    /* صندوق الجملة: خلفية وردية والكتابة باللون الأبيض */
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
    
    /* الأزرار (Next و Back): خلفية وردية والكتابة باللون الأبيض */
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
    
    /* تأثير تمرير الماوس فوق الأزرار */
    div.stButton > button:hover {
        background-color: #7A306C !important;
        color: #FFFFFF !important;
    }
    
    /* إزالة خلفية الصورة البيضاء لتبدو شفافة ومدمجة */
    .transparent-img img {
        mix-blend-mode: multiply;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. عرض العنوان الرئيسي بالوردي
st.markdown("<h1 class='main-title'>AI-Powered Mammogram Analysis for Early Breast Cancer Detection</h1>", unsafe_allow_html=True)
st.write("---")

# 4. عرض العنوان الفرعي
st.markdown("<h3 class='sub-title'>Your health matters ❤️</h3>", unsafe_allow_html=True)

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
    # عرض الصورة داخل حاوية (Container) لتطبيق الفلتر الشفاف عليها
    st.markdown('<div class="transparent-img">', unsafe_allow_html=True)
    try:
        st.image("my2.jpg", width=220)
    except Exception as e:
        st.warning("Image 'my2.jpg' not found.")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # العبارة التشجيعية بخلفية وردية ونص أبيض
    st.markdown("<div class='quote-box'>\"Like butterflies we flourish when we feel safe\"</div>", unsafe_allow_html=True)

st.write("\n\n") 

# 6. أزرار التحكم في أسفل الصفحة (خلفية وردية وكتابة بيضاء)
col_btn1, col_btn2, col_btn3, col_btn4 = st.columns([1, 2, 2, 1])

with col_btn2:
    if st.button("« Back"):
        st.info("Back button clicked")

with col_btn3:
    if st.button("Next »"):
        st.success("Proceeding to the next step...")

import streamlit as st

# 1. إعدادات الصفحة (العنوان والأيقونة التي تظهر في المتصفح)
st.set_page_config(page_title="AI Mammogram Analysis", page_icon="🎗️", layout="centered")

# 2. تخصيص الألوان والتنسيقات باستخدام CSS لتطابق تصميمك الأصلي
st.markdown("""
    <style>
    /* تغيير لون الخلفية العامة للتطبيق لتبدو متناسقة */
    .stApp {
        background-color: #FAFAFA;
    }
    /* تنسيق العنوان الرئيسي */
    .main-title {
        color: #7A306C;
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-weight: bold;
        font-size: 28px;
        margin-bottom: 20px;
    }
    /* تنسيق العنوان الفرعي */
    .sub-title {
        color: #A3488E;
        text-align: left;
        font-family: 'Arial', sans-serif;
        font-weight: bold;
        margin-top: 10px;
        margin-bottom: 20px;
    }
    /* تنسيق صندوق العبارة التشجيعية أسفل الصورة */
    .quote-box {
        background-color: #A3488E;
        color: white;
        padding: 12px;
        border-radius: 15px;
        text-align: center;
        font-style: italic;
        margin-top: 25px;
        font-size: 14px;
        box-shadow: 1px 2px 5px rgba(0,0,0,0.1);
    }
    /* تنسيق أزرار التنقل (Next & Back) */
    div.stButton > button {
        background-color: #B35B9D;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 8px 30px;
        font-weight: bold;
        width: 100%;
        transition: 0.3s;
    }
    /* تأثير عند تمرير الماوس فوق الأزرار */
    div.stButton > button:hover {
        background-color: #7A306C;
        color: white;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. عرض العنوان الرئيسي والخط الفاصل
st.markdown("<h1 class='main-title'>AI-Powered Mammogram Analysis for Early Breast Cancer Detection</h1>", unsafe_allow_html=True)
st.write("---")

# 4. عرض العنوان الفرعي "Your health matters" مع إيموجي القلب
st.markdown("<h3 class='sub-title'>Your health matters ❤️</h3>", unsafe_allow_html=True)

# 5. تقسيم الواجهة إلى عمودين (اليسار للمدخلات واليمين للصورة)
col1, col2 = st.columns([1.2, 1])

with col1:
    # حقول إدخال البيانات الخاصة بالمريض
    patient_name = st.text_input("Patient Name", placeholder="Enter patient name")
    patient_age = st.text_input("Patient Age", placeholder="Enter age")
    phone_number = st.text_input("Phone Number", placeholder="Enter phone number")
    
    # اختيار التاريخ الطبي (Radio Buttons)
    medical_history = st.radio("Medical History", ["No", "Yes"], index=0)

with col2:
    # عرض الصورة الشخصية التي قمت برفعها باسم (my2.jpg)
    try:
        st.image("my2.jpg", width=220)
    except Exception as e:
        # رسالة احتياطية في حال لم يجد ملف الصورة في السيرفر
        st.warning("Image 'my2.jpg' not found. Please ensure it is uploaded in the same repository.")
    
    # العبارة التشجيعية أسفل الصورة مباشرة
    st.markdown("<div class='quote-box'>\"Like butterflies we flourish when we feel safe\"</div>", unsafe_allow_html=True)

# إضافة مسافة عمودية قبل الأزرار
st.write("\n\n") 

# 6. أزرار التحكم والتنقل في أسفل الصفحة
col_btn1, col_btn2, col_btn3, col_btn4 = st.columns([1, 2, 2, 1])

with col_btn2:
    if st.button("« Back"):
        st.info("Back button clicked")

with col_btn3:
    if st.button("Next »"):
        st.success("Proceeding to the next step...")
import time
import streamlit as st

st.set_page_config(page_title="Addition with Sliders", page_icon="➕", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #eaf4ff;
    }
    .stTitle, .stSubheader, .stTextInput, .stSlider label, .stMetric, .stAlert {
        color: #0d1b6a !important;
    }
    div[data-testid="stBlock"] {
        color: #0d1b6a;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Addition of Two Numbers")
st.subheader("Pick the numbers using sliders")

col1, col2 = st.columns(2)
with col1:
    first_number = st.slider("First Number", 0, 100, 25)
with col2:
    second_number = st.slider("Second Number", 0, 100, 35)

sum_value = first_number + second_number

st.markdown(
    f"""
    <div style="padding:20px; border-radius:12px; background:#f7fbff; border:2px solid #b7d4ff; text-align:center;">
        <h2 style="color:#0d1b6a; margin:0;">Result</h2>
        <div style="font-size:48px; font-weight:bold; color:#0d1b6a; margin-top:8px;">{sum_value}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

placeholder = st.empty()
for size in [40, 56, 72, 56, 40]:
    placeholder.markdown(
        f"""
        <div style="text-align:center; margin-top:16px;">
            <span style="font-size:{size}px; font-weight:bold; color:#0d1b6a;">{sum_value}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    time.sleep(0.12)

st.success(f"{first_number} + {second_number} = {sum_value}")

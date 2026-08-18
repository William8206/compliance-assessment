import streamlit as st

from auth import require_login

require_login()

st.title("① 法規評估")

st.write("CE / FCC Compliance Assessment")

st.info(
    "這裡將建立產品條件輸入與法規適用性判定功能。"
)
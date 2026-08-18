import streamlit as st

from auth import require_login

require_login()

st.title("② 法規資料庫")

st.info(
    "這裡將管理 CE / FCC 法規、標準與版本資訊。"
)
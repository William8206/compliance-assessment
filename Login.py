import streamlit as st

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="CE / FCC Compliance Assessment",
    page_icon="⚖️",
    layout="wide"
)

# ==========================================
# Authentication
# ==========================================

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False


def login_page():

    st.title("CE / FCC Compliance Assessment")

    st.caption(
        "Information Product Regulatory Assessment System"
    )

    st.divider()

    st.header("🔐 Internal Access")

    st.write(
        "此系統提供認證評估使用，請輸入通關密語。"
    )

    password = st.text_input(
        "通關密語",
        type="password",
        placeholder="請輸入通關密語"
    )

    if st.button(
        "進入系統",
        type="primary",
        use_container_width=True
    ):

        if password == st.secrets["access_password"]:

            st.session_state.authenticated = True
            st.rerun()

        else:

            st.error(
                "通關密語錯誤，請重新輸入。"
            )


# ==========================================
# Login Check
# ==========================================

if not st.session_state.authenticated:

    login_page()

    st.stop()


# ==========================================
# Home Page
# ==========================================

st.title("CE / FCC Compliance Assessment")

st.caption(
    "Information Product Regulatory Assessment System"
)
st.divider()

st.header("歡迎使用系統評估網站")

st.write(
    """
本系統提供 Information Product 之 CE / FCC
法規適用性評估。

請由左側選單選擇功能。
"""
)

st.info(
    "請先進入「系統評估」開始產品法規判定。"
)

# ==========================================
# Logout
# ==========================================

if st.sidebar.button("登出"):

    st.session_state.authenticated = False

    st.rerun()
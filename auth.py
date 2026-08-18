import streamlit as st


def require_login():

    if not st.session_state.get(
        "authenticated",
        False
    ):

        st.warning(
            "🔐 請先登入系統。"
        )

        st.stop()
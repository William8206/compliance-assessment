import streamlit as st

from utils.database import (
    load_regulations,
    load_standards,
    load_test_items,
    load_sources,
)


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="法規資料庫",
    page_icon="📚",
    layout="wide",
)


# ==========================================
# Header
# ==========================================

st.title("② 法規資料庫")

st.caption(
    "CE / FCC Regulatory Database"
)

st.divider()


# ==========================================
# Load Data
# ==========================================

regulations = load_regulations()

standards = load_standards()

test_items = load_test_items()

sources = load_sources()


# ==========================================
# Statistics
# ==========================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Regulations",
        len(regulations)
    )

with col2:

    st.metric(
        "Standards",
        len(standards)
    )

with col3:

    st.metric(
        "Test Items",
        len(test_items)
    )

with col4:

    st.metric(
        "Sources",
        len(sources)
    )


st.divider()


# ==========================================
# Regulations
# ==========================================

st.subheader("Regulations")

if len(regulations) > 0:
    st.table(regulations)
else:

    st.info(
        "目前沒有法規資料。"
    )


# ==========================================
# Standards
# ==========================================

st.subheader("Standards")

if len(standards) > 0:
    st.table(standards)

else:

    st.info(
        "目前沒有標準資料。"
    )


# ==========================================
# Test Items
# ==========================================

st.subheader("Test Items")

if len(test_items) > 0:
    st.table(test_items)
else:

    st.info(
        "目前沒有測試項目。"
    )


# ==========================================
# Sources
# ==========================================

st.subheader("Sources")
if len(sources) > 0:
    st.table(sources)
else:

    st.info(
        "目前沒有來源資料。"
    )
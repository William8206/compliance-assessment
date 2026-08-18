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
# Internal Access - 通關密語
# ==========================================

if "login" not in st.session_state:
    st.session_state.login = False


if not st.session_state.login:

    st.title("CE / FCC Compliance Assessment")

    st.caption(
        "Information Product Regulatory Assessment System"
    )

    st.divider()

    st.subheader("🔐 Internal Access")

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

        if password == "Portwell":

            st.session_state.login = True

            st.rerun()

        else:

            st.error(
                "通關密語錯誤，請重新輸入。"
            )

    st.stop()


# ==========================================
# Header
# ==========================================

st.title("CE / FCC Compliance Assessment")

st.caption(
    "Information Product Regulatory Assessment System"
)

st.divider()


# ==========================================
# Product Information
# ==========================================

st.header("① Product Information")

col1, col2 = st.columns(2)

with col1:

    product_model = st.text_input(
        "Product Model",
        placeholder="例如：LYNX-811A"
    )

    product_type = st.selectbox(
        "Product Type",
        [
            "Industrial PC",
            "Box PC",
            "Panel PC",
            "Motherboard",
            "Other"
        ]
    )


with col2:

    target_market = st.multiselect(
        "Target Market",
        [
            "European Union",
            "United States"
        ]
    )


# ==========================================
# Power
# ==========================================

st.header("② Power Information")

col1, col2, col3 = st.columns(3)


with col1:

    power_type = st.selectbox(
        "Power Input",
        [
            "DC",
            "AC"
        ]
    )


with col2:

    min_voltage = st.number_input(
        "Minimum Voltage (V)",
        min_value=0.0,
        value=9.0
    )


with col3:

    max_voltage = st.number_input(
        "Maximum Voltage (V)",
        min_value=0.0,
        value=36.0
    )


external_adapter = st.checkbox(
    "External AC Adapter"
)


# ==========================================
# Wireless
# ==========================================

st.header("③ Wireless Function")

col1, col2, col3 = st.columns(3)


with col1:

    wifi = st.checkbox(
        "Wi-Fi"
    )


with col2:

    bluetooth = st.checkbox(
        "Bluetooth"
    )


with col3:

    lte_5g = st.checkbox(
        "LTE / 5G"
    )


# ==========================================
# Interface
# ==========================================

st.header("④ Interface")

col1, col2, col3, col4 = st.columns(4)


with col1:

    ethernet = st.checkbox(
        "Ethernet"
    )


with col2:

    usb = st.checkbox(
        "USB"
    )


with col3:

    display = st.checkbox(
        "HDMI / DisplayPort"
    )


with col4:

    poe = st.checkbox(
        "PoE"
    )


# ==========================================
# Other
# ==========================================

st.header("⑤ Other")

col1, col2 = st.columns(2)


with col1:

    battery = st.checkbox(
        "Battery"
    )


with col2:

    other_rf = st.checkbox(
        "Other RF Function"
    )


st.divider()


# ==========================================
# Assessment Button
# ==========================================

if st.button(
    "開始法規判定",
    type="primary",
    use_container_width=True
):

    if not product_model:

        st.error(
            "請輸入 Product Model"
        )

    elif not target_market:

        st.error(
            "請至少選擇一個 Target Market"
        )

    else:

        st.header(
            "⑥ Compliance Assessment"
        )


        # ==================================
        # CE
        # ==================================

        if "European Union" in target_market:

            st.subheader(
                "🇪🇺 CE Compliance"
            )

            col1, col2, col3 = st.columns(3)


            # CE EMC
            with col1:

                st.success(
                    "CE EMC"
                )

                st.write(
                    "REQUIRED"
                )


            # CE LVD
            with col2:

                if (
                    power_type == "DC"
                    and max_voltage < 75
                ):

                    st.warning(
                        "CE LVD"
                    )

                    st.write(
                        "N/A"
                    )

                else:

                    st.info(
                        "CE LVD"
                    )

                    st.write(
                        "REVIEW"
                    )


            # CE RED
            with col3:

                if (
                    wifi
                    or bluetooth
                    or lte_5g
                    or other_rf
                ):

                    st.success(
                        "CE RED"
                    )

                    st.write(
                        "REQUIRED"
                    )

                else:

                    st.info(
                        "CE RED"
                    )

                    st.write(
                        "N/A"
                    )


        # ==================================
        # FCC
        # ==================================

        if "United States" in target_market:

            st.subheader(
                "🇺🇸 FCC Compliance"
            )

            col1, col2 = st.columns(2)


            # FCC Part 15
            with col1:

                st.success(
                    "FCC Part 15"
                )

                st.write(
                    "REQUIRED"
                )


            # FCC RF
            with col2:

                if (
                    wifi
                    or bluetooth
                    or lte_5g
                    or other_rf
                ):

                    st.success(
                        "FCC RF"
                    )

                    st.write(
                        "REQUIRED"
                    )

                else:

                    st.info(
                        "FCC RF"
                    )

                    st.write(
                        "N/A"
                    )


        # ==================================
        # Required Test Items
        # ==================================

        st.divider()

        st.subheader(
            "⑦ Required Test Items"
        )

        test_items = []


        # CE Test Items
        if "European Union" in target_market:

            test_items.extend([
                [
                    "Conducted Emission",
                    "EN 55032",
                    "CE EMC"
                ],

                [
                    "Radiated Emission",
                    "EN 55032",
                    "CE EMC"
                ],

                [
                    "ESD",
                    "EN 55035",
                    "CE EMC"
                ],

                [
                    "Radiated Immunity",
                    "EN 55035",
                    "CE EMC"
                ],

                [
                    "EFT",
                    "EN 55035",
                    "CE EMC"
                ],

                [
                    "Surge",
                    "EN 55035",
                    "CE EMC"
                ],

                [
                    "Conducted Immunity",
                    "EN 55035",
                    "CE EMC"
                ],
            ])


        # FCC Test Items
        if "United States" in target_market:

            test_items.extend([
                [
                    "FCC Conducted Emission",
                    "FCC Part 15",
                    "FCC"
                ],

                [
                    "FCC Radiated Emission",
                    "FCC Part 15",
                    "FCC"
                ],
            ])


        # Wireless Test
        if (
            wifi
            or bluetooth
            or lte_5g
        ):

            test_items.append([
                "Wireless RF",
                "Applicable RF Standard",
                "CE RED / FCC"
            ])


        # Display Results
        if test_items:

            st.dataframe(
                test_items,

                column_config={
                    0: "Test Item",
                    1: "Standard",
                    2: "Regulation"
                },

                hide_index=True,

                use_container_width=True
            )
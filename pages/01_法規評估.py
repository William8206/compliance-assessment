import streamlit as st

from auth import require_login


# ==========================================
# Login Check
# ==========================================

require_login()


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="法規評估",
    page_icon="⚖️",
    layout="wide"
)


# ==========================================
# Compact Layout
# ==========================================

st.markdown(
    """
    <style>

    /* ======================================
       Overall Layout
       ====================================== */

    div[data-testid="stVerticalBlock"] {
        gap: 0.15rem;
    }

    div[data-testid="stHorizontalBlock"] {
        gap: 0.35rem;
    }


    /* ======================================
       Main Headers
       ====================================== */

    h1 {
        margin-top: 0.2rem;
        margin-bottom: 0.2rem;
    }

    h2 {
        margin-top: 0.5rem;
        margin-bottom: 0.2rem;
    }

    h3 {
        margin-top: 0.25rem;
        margin-bottom: 0.1rem;
    }


    /* ======================================
       Checkbox
       ====================================== */

    div[data-testid="stCheckbox"] {
        margin-top: -0.3rem;
        margin-bottom: -0.3rem;
    }


    /* ======================================
       Input Widgets
       ====================================== */

    div[data-testid="stTextInput"],
    div[data-testid="stSelectbox"],
    div[data-testid="stMultiSelect"],
    div[data-testid="stNumberInput"] {
        margin-bottom: -0.15rem;
    }


    /* ======================================
       Divider
       ====================================== */

    hr {
        margin-top: 0.4rem;
        margin-bottom: 0.4rem;
    }


    /* ======================================
       Alert
       ====================================== */

    div[data-testid="stAlert"] {
        padding-top: 0.5rem;
        padding-bottom: 0.5rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==========================================
# Header
# ==========================================

st.title("① 法規評估")

st.caption(
    "Information Product Regulatory Assessment System"
)

st.info(
    "請依據產品實際規格輸入條件，系統將依據法規資料庫進行適用性判定。"
)

st.divider()


# ==========================================
# ① Product Information
# ==========================================

st.header("① Product Information")

col1, col2 = st.columns(2)

with col1:

    product_model = st.text_input(
        "Product Model",
        placeholder="例如：LYNX-811A"
    )

with col2:

    product_type = st.selectbox(
        "Product Type",
        [
            "Industrial PC",
            "Box PC",
            "Panel PC",
            "Motherboard",
            "Embedded Computer",
            "Other"
        ]
    )

target_market = st.multiselect(
    "Target Market",
    [
        "European Union (CE)",
        "United States (FCC)"
    ],
    help="選擇此產品預計銷售的市場。"
)


# ==========================================
# ② Power Information
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
        max_value=1000.0,
        value=9.0,
        step=0.1
    )

with col3:

    max_voltage = st.number_input(
        "Maximum Voltage (V)",
        min_value=0.0,
        max_value=1000.0,
        value=36.0,
        step=0.1
    )

external_adapter = st.checkbox(
    "External AC Adapter"
)


# ==========================================
# ③ Wireless / RF Function
# ==========================================

st.header("③ Wireless / RF Function")

col1, col2, col3, col4 = st.columns(4)

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

with col4:

    other_rf = st.checkbox(
        "Other RF"
    )


# ==========================================
# ④ Interface
# ==========================================

st.header("④ Interface")


# ------------------------------------------
# General Interface
# ------------------------------------------

st.subheader("General Interface")

col1, col2, col3 = st.columns(3)

with col1:

    ethernet = st.checkbox(
        "Ethernet"
    )

with col2:

    type_c = st.checkbox(
        "Type-C"
    )

with col3:

    audio = st.checkbox(
        "Audio"
    )


# ------------------------------------------
# Serial Interface
# ------------------------------------------

st.subheader("Serial Interface")

col1, col2, col3 = st.columns(3)

with col1:

    rs232 = st.checkbox(
        "RS-232"
    )

with col2:

    rs422 = st.checkbox(
        "RS-422"
    )

with col3:

    rs485 = st.checkbox(
        "RS-485"
    )


# ------------------------------------------
# Digital I/O
# ------------------------------------------

st.subheader("Digital I/O")

col1, col2 = st.columns(2)

with col1:

    dido = st.checkbox(
        "DIDO"
    )

with col2:

    gpio = st.checkbox(
        "GPIO"
    )


# ------------------------------------------
# USB
# ------------------------------------------

st.subheader("USB")

col1, col2 = st.columns(2)

with col1:

    usb_2 = st.checkbox(
        "USB 2.0"
    )

with col2:

    usb_3 = st.checkbox(
        "USB 3.x"
    )


# ------------------------------------------
# Display Interface
# ------------------------------------------

st.subheader("Display Interface")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:

    vga = st.checkbox(
        "VGA"
    )

with col2:

    hdmi = st.checkbox(
        "HDMI"
    )

with col3:

    dp = st.checkbox(
        "DisplayPort"
    )

with col4:

    dvi = st.checkbox(
        "DVI"
    )

with col5:

    display_type_c = st.checkbox(
        "Type-C Display"
    )


# ------------------------------------------
# Industrial Bus
# ------------------------------------------

st.subheader("Industrial Bus")

can_bus = st.checkbox(
    "CAN Bus"
)


# ------------------------------------------
# Power over Ethernet
# ------------------------------------------

st.subheader("Power over Ethernet")

poe = st.checkbox(
    "PoE"
)


# ==========================================
# ⑤ Other Functions
# ==========================================

st.header("⑤ Other Functions")

col1, col2, col3 = st.columns(3)

with col1:

    battery = st.checkbox(
        "Battery"
    )

with col2:

    touchscreen = st.checkbox(
        "Touchscreen"
    )

with col3:

    audio_function = st.checkbox(
        "Audio Function"
    )


# ==========================================
# ⑥ Product Characteristics
# ==========================================

st.header("⑥ Product Characteristics")

col1, col2, col3 = st.columns(3)

with col1:

    internal_power_supply = st.checkbox(
        "Internal Power Supply"
    )

with col2:

    external_power_supply = st.checkbox(
        "External Power Supply"
    )

with col3:

    industrial_environment = st.checkbox(
        "Industrial Environment"
    )


# ==========================================
# ⑦ Product Condition Summary
# ==========================================

st.divider()

st.header("⑦ Product Condition Summary")


# ==========================================
# Prepare Display Values
# ==========================================

target_market_display = (
    ", ".join(target_market)
    if target_market
    else "None"
)


serial_display = ", ".join(
    [
        name
        for name, enabled in [
            ("RS-232", rs232),
            ("RS-422", rs422),
            ("RS-485", rs485),
        ]
        if enabled
    ]
) or "None"


dido_gpio_display = ", ".join(
    [
        name
        for name, enabled in [
            ("DIDO", dido),
            ("GPIO", gpio),
        ]
        if enabled
    ]
) or "None"


usb_display = ", ".join(
    [
        name
        for name, enabled in [
            ("USB 2.0", usb_2),
            ("USB 3.x", usb_3),
        ]
        if enabled
    ]
) or "None"


display_display = ", ".join(
    [
        name
        for name, enabled in [
            ("VGA", vga),
            ("HDMI", hdmi),
            ("DisplayPort", dp),
            ("DVI", dvi),
            ("Type-C Display", display_type_c),
        ]
        if enabled
    ]
) or "None"


# ==========================================
# Summary Row
# ==========================================

def summary_row(label, value, active=False):

    if active:
        bg = "#E8F5E9"
        text = "#137333"
    else:
        bg = "#F8F9FA"
        text = "#333333"

    html = f"""
<div style="display:flex;align-items:center;justify-content:space-between;width:100%;min-height:30px;padding:5px 10px;margin:2px 0;background:{bg};border-radius:5px;font-size:14px;">
<div style="font-size:15px;font-weight:500;white-space:nowrap;color:#333333;">{label}</div><div style="font-weight:600;text-align:right;margin-left:15px;color:{text};">{value}</div>
</div>
"""

    st.markdown(
        html,
        unsafe_allow_html=True
    )


# ==========================================
# Two Column Layout
# ==========================================

outer_left, left_col, right_col, outer_right = st.columns([3.5, 2, 2 ,3.5])


# ==========================================
# LEFT
# ==========================================

with left_col:

    st.markdown("**Product / Power / Wireless**")

    summary_row(
        "Product Model",
        product_model or "未輸入",
        bool(product_model)
    )

    summary_row(
        "Product Type",
        product_type,
        True
    )

    summary_row(
        "Target Market",
        target_market_display,
        bool(target_market)
    )

    summary_row(
        "Power Input",
        power_type,
        True
    )

    summary_row(
        "Input Voltage",
        f"{min_voltage:.1f} ~ {max_voltage:.1f} V",
        True
    )

    summary_row(
        "External AC Adapter",
        "Yes" if external_adapter else "No",
        external_adapter
    )

    summary_row(
        "Wi-Fi",
        "Yes" if wifi else "No",
        wifi
    )

    summary_row(
        "Bluetooth",
        "Yes" if bluetooth else "No",
        bluetooth
    )

    summary_row(
        "LTE / 5G",
        "Yes" if lte_5g else "No",
        lte_5g
    )

    summary_row(
        "Other RF",
        "Yes" if other_rf else "No",
        other_rf
    )


# ==========================================
# RIGHT
# ==========================================

with right_col:

    st.markdown("**Interface / Function**")

    summary_row(
        "Ethernet",
        "Yes" if ethernet else "No",
        ethernet
    )

    summary_row(
        "Type-C",
        "Yes" if type_c else "No",
        type_c
    )

    summary_row(
        "Audio",
        "Yes" if audio else "No",
        audio
    )

    summary_row(
        "Serial Interface",
        serial_display,
        rs232 or rs422 or rs485
    )

    summary_row(
        "DIDO / GPIO",
        dido_gpio_display,
        dido or gpio
    )

    summary_row(
        "USB",
        usb_display,
        usb_2 or usb_3
    )

    summary_row(
        "Display Interface",
        display_display,
        vga or hdmi or dp or dvi or display_type_c
    )

    summary_row(
        "CAN Bus",
        "Yes" if can_bus else "No",
        can_bus
    )

    summary_row(
        "PoE",
        "Yes" if poe else "No",
        poe
    )

    summary_row(
        "Battery",
        "Yes" if battery else "No",
        battery
    )

    summary_row(
        "Touchscreen",
        "Yes" if touchscreen else "No",
        touchscreen
    )

    summary_row(
        "Industrial Environment",
        "Yes" if industrial_environment else "No",
        industrial_environment
    )


# ==========================================
# ⑧ Compliance Assessment
# ==========================================

st.divider()

st.header("⑧ Compliance Assessment")


if st.button(
    "開始法規判定",
    type="primary",
    use_container_width=True
):

    if not product_model:

        st.error(
            "請先輸入 Product Model。"
        )

    elif not target_market:

        st.error(
            "請至少選擇一個 Target Market。"
        )

    else:

        st.success(
            "產品條件已完成。"
        )

        st.info(
            "目前 Rule Engine 尚未啟用，下一階段將依據法規資料庫進行自動判定。"
        )


# ==========================================
# System Information
# ==========================================

with st.expander("系統資訊"):

    st.write(
        "本頁目前負責產品條件輸入。"
    )

    st.write(
        "後續將串接 Regulation → Standard → Test Item → Rule Engine。"
    )

# ==========================================
# ⑧ Compliance Assessment
# ==========================================

st.divider()

st.header("⑧ Compliance Assessment")


if st.button(
    "開始法規判定",
    type="primary",
    use_container_width=True
):

    # --------------------------------------
    # Basic Validation
    # --------------------------------------

    if not product_model:

        st.error(
            "請先輸入 Product Model。"
        )

    elif not target_market:

        st.error(
            "請至少選擇一個 Target Market。"
        )

    else:

        st.success(
            "產品條件已完成。"
        )

        st.info(
            "目前 Rule Engine 尚未啟用，下一階段將依據法規資料庫進行自動判定。"
        )


# ==========================================
# System Information
# ==========================================

with st.expander("系統資訊"):

    st.write(
        "本頁目前負責產品條件輸入。"
    )

    st.write(
        "後續將串接 Regulation → Standard → Test Item → Rule Engine。"
    )
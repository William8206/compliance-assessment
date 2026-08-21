import streamlit as st

from auth import require_login

from utils.rules import evaluate_product

from utils.database import (
    load_regulations,
    load_standards,
    load_test_items,
)


# =========================================================
# Page Configuration
# =========================================================

st.set_page_config(
    page_title="系統評估",
    page_icon="??",
    layout="wide",
)


# =========================================================
# Login
# =========================================================

require_login()


# =========================================================
# Page Style
# =========================================================

st.markdown(
    """
<style>

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

/* -----------------------------------------
   Compact Layout
----------------------------------------- */

div[data-testid="stVerticalBlock"] {
    gap: 0.7rem;
}

div[data-testid="stHorizontalBlock"] {
    gap: 0.8rem;
}

/* -----------------------------------------
   Headers
----------------------------------------- */

h1 {
    margin-bottom: 0.2rem;
}

h2 {
    margin-top: 0.6rem;
    margin-bottom: 0.3rem;
}

h3 {
    margin-top: 0.5rem;
    margin-bottom: 0.2rem;
}

/* -----------------------------------------
   Divider
----------------------------------------- */

hr {
    margin-top: 0.6rem;
    margin-bottom: 0.6rem;
}

/* -----------------------------------------
   Checkbox
----------------------------------------- */

div[data-testid="stCheckbox"] {
    margin-top: -0.25rem;
    margin-bottom: -0.25rem;
}

/* -----------------------------------------
   Result Table
----------------------------------------- */

.compliance-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 8px;
    margin-bottom: 12px;
    font-size: 14px;
}

.compliance-table th {
    background: #F1F3F5;
    color: #333333;
    font-weight: 600;
    text-align: left;
    padding: 9px 10px;
    border: 1px solid #D9DDE2;
}

.compliance-table td {
    padding: 9px 10px;
    border: 1px solid #E1E4E8;
    vertical-align: middle;
}

.compliance-table tr:hover {
    background: #FAFAFA;
}

/* -----------------------------------------
   Required
----------------------------------------- */

.required-badge {
    display: inline-block;
    background: #FF4B4B;
    color: #000000;
    font-weight: 700;
    padding: 3px 9px;
    border-radius: 4px;
    font-size: 13px;
    white-space: nowrap;
}

/* -----------------------------------------
   Optional
----------------------------------------- */

.optional-badge {
    display: inline-block;
    background: #E9ECEF;
    color: #333333;
    font-weight: 600;
    padding: 3px 9px;
    border-radius: 4px;
    font-size: 13px;
    white-space: nowrap;
}

/* -----------------------------------------
   Standard Header
----------------------------------------- */

.standard-header {
    margin-top: 12px;
    margin-bottom: 3px;
    font-size: 20px;
    font-weight: 700;
}

/* -----------------------------------------
   Market Header
----------------------------------------- */

.market-header {
    margin-top: 14px;
    margin-bottom: 8px;
    font-size: 24px;
    font-weight: 700;
}

/* -----------------------------------------
   Summary Row
----------------------------------------- */

.summary-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    min-height: 30px;
    padding: 5px 10px;
    margin: 2px 0;
    border-radius: 5px;
    font-size: 14px;
}

.summary-label {
    font-size: 15px;
    font-weight: 500;
    white-space: nowrap;
    color: #333333;
}

.summary-value {
    font-weight: 600;
    text-align: right;
    margin-left: 15px;
}

/* -----------------------------------------
   Result Count
----------------------------------------- */

.result-count {
    display: inline-block;
    background: #F1F3F5;
    color: #333333;
    padding: 4px 9px;
    border-radius: 5px;
    font-size: 13px;
    margin-bottom: 6px;
}

</style>
""",
    unsafe_allow_html=True,
)


# =========================================================
# Header
# =========================================================

st.title("系統評估")

st.caption(
    "Information Product Regulatory Assessment System"
)

st.info(
    "請依據產品實際規格輸入條件，系統將依據法規資料庫進行適用性判定。"
)

st.divider()


# =========================================================
# ? Product Information
# =========================================================

st.header("1產品資訊")

col1, col2 = st.columns(2)

with col1:

    product_model = st.text_input(
        "產品型號",
        placeholder="例如：LYNX-811A",
    )

with col2:

    target_market = st.multiselect(
        "目標市場",
        [
            "EU (CE)",
            "US (FCC)",
        ],
    )


product_type = st.selectbox(
    "產品類型",
    [
        "Industrial PC",
        "Box PC",
        "Panel PC",
        "Embedded Computer",
    ],
)


# =========================================================
# ? Power Information
# =========================================================

st.header("2電源資訊")

col1, col2, col3 = st.columns(3)

with col1:

    power_type = st.selectbox(
        "電源輸入",
        [
            "DC",
            "AC",
        ],
    )

with col2:

    min_voltage = st.number_input(
        "最低電壓 (V)",
        min_value=5.0,
        max_value=300.0,
        value=9.0,
        step=0.1,
    )

with col3:

    max_voltage = st.number_input(
        "最高電壓 (V)",
        min_value=5.0,
        max_value=330.0,
        value=36.0,
        step=0.1,
    )

external_adapter = st.checkbox(
    "External AC Adapter"
)


# =========================================================
# ? Wireless / RF
# =========================================================

st.header("3無線 / RF 功能")

col1, col2, col3, col4 = st.columns(4)

with col1:
    wifi = st.checkbox("Wi-Fi")

with col2:
    bluetooth = st.checkbox("Bluetooth")

with col3:
    lte_5g = st.checkbox("LTE / 5G")

with col4:
    other_rf = st.checkbox("Other RF")


# =========================================================
# ? Interface
# =========================================================

st.header("4介面")

# ---------------------------------------------------------
# General Interface
# ---------------------------------------------------------

st.subheader("General Interface")

col1, col2, col3 = st.columns(3)

with col1:
    ethernet = st.checkbox("Ethernet")

with col2:
    type_c = st.checkbox("Type-C")

with col3:
    audio = st.checkbox("Audio")


# ---------------------------------------------------------
# Serial
# ---------------------------------------------------------

st.subheader("Serial Interface")

col1, col2, col3 = st.columns(3)

with col1:
    rs232 = st.checkbox("RS-232")

with col2:
    rs422 = st.checkbox("RS-422")

with col3:
    rs485 = st.checkbox("RS-485")


# ---------------------------------------------------------
# DIDO / GPIO
# ---------------------------------------------------------

st.subheader("Digital I/O")

col1, col2 = st.columns(2)

with col1:
    dido = st.checkbox("DIDO")

with col2:
    gpio = st.checkbox("GPIO")


# ---------------------------------------------------------
# USB
# ---------------------------------------------------------

st.subheader("USB")

col1, col2 = st.columns(2)

with col1:
    usb_2 = st.checkbox("USB 2.0")

with col2:
    usb_3 = st.checkbox("USB 3.x")


# ---------------------------------------------------------
# Display
# ---------------------------------------------------------

st.subheader("Display Interface")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    vga = st.checkbox("VGA")

with col2:
    hdmi = st.checkbox("HDMI")

with col3:
    dp = st.checkbox("DisplayPort")

with col4:
    dvi = st.checkbox("DVI")

with col5:
    display_type_c = st.checkbox("Type-C Display")


# ---------------------------------------------------------
# Industrial Interface
# ---------------------------------------------------------

st.subheader("Industrial Interface")

col1, col2 = st.columns(2)

with col1:
    can_bus = st.checkbox("CAN Bus")

with col2:
    poe = st.checkbox("PoE")


# =========================================================
# ? Other Functions
# =========================================================

st.header("5其他功能")

col1, col2, col3 = st.columns(3)

with col1:
    battery = st.checkbox("Battery")

with col2:
    touchscreen = st.checkbox("Touchscreen")

with col3:
    industrial_environment = st.checkbox(
        "Industrial Environment"
    )


# =========================================================
# ? Product Condition Summary
# =========================================================

st.divider()

st.header("6產品狀況概要")


# =========================================================
# Summary Helper
# =========================================================

def summary_row(
    label,
    value,
    active=False,
):

    if active:

        bg = "#E8F5E9"
        text = "#137333"

    else:

        bg = "#F8F9FA"
        text = "#333333"


    html = (
        f'<div class="summary-row" '
        f'style="background:{bg};">'
        f'<div class="summary-label">'
        f'{label}'
        f'</div>'
        f'<div class="summary-value" '
        f'style="color:{text};">'
        f'{value}'
        f'</div>'
        f'</div>'
    )

    st.markdown(
        html,
        unsafe_allow_html=True,
    )


# =========================================================
# Summary Values
# =========================================================

target_market_display = (
    ", ".join(target_market)
    if target_market
    else "None"
)


serial_list = []

if rs232:
    serial_list.append("RS-232")

if rs422:
    serial_list.append("RS-422")

if rs485:
    serial_list.append("RS-485")


serial_display = (
    ", ".join(serial_list)
    if serial_list
    else "None"
)


dido_gpio_list = []

if dido:
    dido_gpio_list.append("DIDO")

if gpio:
    dido_gpio_list.append("GPIO")


dido_gpio_display = (
    ", ".join(dido_gpio_list)
    if dido_gpio_list
    else "None"
)


usb_list = []

if usb_2:
    usb_list.append("USB 2.0")

if usb_3:
    usb_list.append("USB 3.x")


usb_display = (
    ", ".join(usb_list)
    if usb_list
    else "None"
)


display_list = []

if vga:
    display_list.append("VGA")

if hdmi:
    display_list.append("HDMI")

if dp:
    display_list.append("DisplayPort")

if dvi:
    display_list.append("DVI")

if display_type_c:
    display_list.append("Type-C")


display_display = (
    ", ".join(display_list)
    if display_list
    else "None"
)


# =========================================================
# Summary Layout
# =========================================================

empty1, left_col, right_col, empty2 = st.columns(
    [2, 3, 3, 2]
)


# =========================================================
# Product / Power / Wireless
# =========================================================

with left_col:

    st.markdown(
        "**產品 / 電源 / 無線**"
    )

    summary_row(
        "產品型號",
        product_model or "未輸入",
        bool(product_model),
    )

    summary_row(
        "產品類型",
        product_type,
        True,
    )

    summary_row(
        "目標市場",
        target_market_display,
        bool(target_market),
    )

    summary_row(
        "電源輸入",
        power_type,
        True,
    )

    summary_row(
        "輸入電壓",
        f"{min_voltage:.1f} ~ {max_voltage:.1f} V",
        True,
    )

    summary_row(
        "External AC Adapter",
        "Yes" if external_adapter else "No",
        external_adapter,
    )

    summary_row(
        "Wi-Fi",
        "Yes" if wifi else "No",
        wifi,
    )

    summary_row(
        "Bluetooth",
        "Yes" if bluetooth else "No",
        bluetooth,
    )

    summary_row(
        "LTE / 5G",
        "Yes" if lte_5g else "No",
        lte_5g,
    )

    summary_row(
        "Other RF",
        "Yes" if other_rf else "No",
        other_rf,
    )


# =========================================================
# Interface / Function
# =========================================================

with right_col:

    st.markdown(
        "**介面 / 功能**"
    )

    summary_row(
        "Ethernet",
        "Yes" if ethernet else "No",
        ethernet,
    )

    summary_row(
        "Type-C",
        "Yes" if type_c else "No",
        type_c,
    )

    summary_row(
        "Audio",
        "Yes" if audio else "No",
        audio,
    )

    summary_row(
        "Serial Interface",
        serial_display,
        bool(serial_list),
    )

    summary_row(
        "DIDO / GPIO",
        dido_gpio_display,
        bool(dido_gpio_list),
    )

    summary_row(
        "USB",
        usb_display,
        bool(usb_list),
    )

    summary_row(
        "Display Interface",
        display_display,
        bool(display_list),
    )

    summary_row(
        "CAN Bus",
        "Yes" if can_bus else "No",
        can_bus,
    )

    summary_row(
        "PoE",
        "Yes" if poe else "No",
        poe,
    )

    summary_row(
        "Battery",
        "Yes" if battery else "No",
        battery,
    )

    summary_row(
        "Touchscreen",
        "Yes" if touchscreen else "No",
        touchscreen,
    )

    summary_row(
        "Industrial Environment",
        "Yes" if industrial_environment else "No",
        industrial_environment,
    )


# =========================================================
# ? Compliance Assessment
# =========================================================

st.divider()

st.header("7系統評估結果")


# =========================================================
# Load Database
# =========================================================

regulations = load_regulations()

standards = load_standards()

test_items = load_test_items()


# =========================================================
# Start Assessment
# =========================================================

if st.button(
    "開始法規判定",
    type="primary",
    use_container_width=True,
):

    # -----------------------------------------------------
    # Validation
    # -----------------------------------------------------

    if not product_model:

        st.error(
            "請先輸入產品型號。"
        )

        st.stop()


    if not target_market:

        st.error(
            "請至少選擇一個目標市場。"
        )

        st.stop()


    # =====================================================
    # Product Data
    # =====================================================

    product_common = {

        "PRODUCT_MODEL":
            product_model,

        "PRODUCT_TYPE":
            product_type,

        "POWER_TYPE":
            power_type,

        "MIN_VOLTAGE":
            min_voltage,

        "MAX_VOLTAGE":
            max_voltage,

        "EXTERNAL_ADAPTER":
            external_adapter,

        "WIFI":
            wifi,

        "BLUETOOTH":
            bluetooth,

        "LTE_5G":
            lte_5g,

        "OTHER_RF":
            other_rf,

        "ETHERNET":
            ethernet,

        "TYPE_C":
            type_c,

        "AUDIO":
            audio,

        "RS232":
            rs232,

        "RS422":
            rs422,

        "RS485":
            rs485,

        "DIDO":
            dido,

        "GPIO":
            gpio,

        "USB_2":
            usb_2,

        "USB_3":
            usb_3,

        "VGA":
            vga,

        "HDMI":
            hdmi,

        "DP":
            dp,

        "DVI":
            dvi,

        "DISPLAY_TYPE_C":
            display_type_c,

        "CAN_BUS":
            can_bus,

        "POE":
            poe,

        "BATTERY":
            battery,

        "TOUCHSCREEN":
            touchscreen,

        "INDUSTRIAL_ENVIRONMENT":
            industrial_environment,
    }


    # =====================================================
    # Market Mapping
    # =====================================================

    market_mapping = {

        "EU (CE)": "EU",

        "US (FCC)": "US",
    }


    # =====================================================
    # Evaluate
    # =====================================================

    all_results = []


    for market_name in target_market:

        product = product_common.copy()

        product["MARKET"] = market_mapping.get(
            market_name,
            market_name,
        )


        results = evaluate_product(
            product
        )


        for result in results:

            result["market"] = market_name

            all_results.append(
                result
            )


    # =====================================================
    # No Result
    # =====================================================

    if not all_results:

        st.warning(
            "目前沒有符合條件的法規規則。"
        )

        st.stop()


    # =====================================================
    # Result Summary
    # =====================================================

    rule_total = len(all_results)

    regulation_total = len(
        set(
            result["regulation_id"]
            for result in all_results
            if result.get("regulation_id")
        )
    )

    required_total = 0
    optional_total = 0
    unmapped_total = 0


    for result in all_results:

        test_item_id = result.get(
            "test_item_id"
        )

        # ---------------------------------------------
        # Rule 沒有對應 Test Item
        # → 法規適用性 Rule
        # ---------------------------------------------

        if not test_item_id:

            unmapped_total += 1

            continue


        rows = test_items[
            test_items["test_item_id"]
            == test_item_id
        ]


        # ---------------------------------------------
        # Rule 有 Test Item ID
        # 但資料庫找不到
        # ---------------------------------------------

        if len(rows) == 0:

            unmapped_total += 1

            continue


        applicability = str(
            rows.iloc[0]["applicability"]
        ).strip().upper()


        if applicability == "REQUIRED":

            required_total += 1


        elif applicability == "OPTIONAL":

            optional_total += 1


        else:

            unmapped_total += 1


    # =====================================================
    # Result Summary UI
    # =====================================================

    st.success(
        "法規判定完成"
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "適用法規",
            f"{regulation_total} 項"
        )


    with col2:

        st.metric(
            "Required 測試",
            f"{required_total} 項"
        )


    with col3:

        st.metric(
            "Optional 測試",
            f"{optional_total} 項"
        )


    # -----------------------------------------------------
    # Additional Information
    # -----------------------------------------------------

    if unmapped_total > 0:

        st.caption(
            f"另外有 {unmapped_total} 項 Rule "
            f"屬於法規適用性判定或尚未對應 Test Item。"
        )


    # =====================================================
    # Market
    # =====================================================

    for market_name in target_market:

        market_results = [

            result

            for result in all_results

            if result["market"]
            == market_name
        ]


        if not market_results:

            st.warning(
                f"{market_name}："
                f"目前沒有符合條件的規則。"
            )

            continue


        # =================================================
        # Market Header
        # =================================================

        st.markdown(
            f'<div class="market-header">'
            f'?? {market_name}'
            f'</div>',
            unsafe_allow_html=True,
        )


        # =================================================
        # Regulation
        # =================================================

        regulation_ids = list(
            dict.fromkeys(

                result["regulation_id"]

                for result in market_results

                if result.get("regulation_id")
            )
        )


        for regulation_id in regulation_ids:

            regulation_rows = regulations[
                regulations["regulation_id"]
                == regulation_id
            ]


            # ------------------------------------------------
            # Regulation Information
            # ------------------------------------------------

            if len(regulation_rows) > 0:

                regulation = (
                    regulation_rows.iloc[0]
                )

                regulation_name = str(
                    regulation["regulation_name"]
                )

                regulation_number = str(
                    regulation["regulation_number"]
                )

                regulation_status = str(
                    regulation["status"]
                )

                regulation_reviewed = str(
                    regulation["last_reviewed"]
                )

            else:

                regulation_name = regulation_id

                regulation_number = ""

                regulation_status = ""

                regulation_reviewed = ""


            st.markdown(
                f"### ?? {regulation_name}"
            )


            if regulation_number:

                st.caption(
                    f"Regulation: "
                    f"{regulation_number}"
                    f"  |  "
                    f"Status: "
                    f"{regulation_status}"
                    f"  |  "
                    f"Last Reviewed: "
                    f"{regulation_reviewed}"
                )


            # =================================================
            # Standards
            # =================================================

            regulation_results = [

                result

                for result in market_results

                if result["regulation_id"]
                == regulation_id
            ]


            standard_ids = list(
                dict.fromkeys(

                    result["standard_id"]

                    for result in regulation_results

                    if result.get("standard_id")
                )
            )


            for standard_id in standard_ids:

                standard_rows = standards[
                    standards["standard_id"]
                    == standard_id
                ]


                if len(standard_rows) == 0:

                    continue


                standard = (
                    standard_rows.iloc[0]
                )


                standard_code = str(
                    standard["standard_code"]
                )

                standard_name = str(
                    standard["standard_name"]
                )


                # =================================================
                # Get Test Items
                # =================================================

                standard_results = [

                    result

                    for result in regulation_results

                    if result["standard_id"]
                    == standard_id
                ]


                test_item_ids = list(
                    dict.fromkeys(

                        result["test_item_id"]

                        for result in standard_results

                        if result.get("test_item_id")
                    )
                )


                test_rows = []


                for test_item_id in test_item_ids:

                    rows = test_items[
                        test_items["test_item_id"]
                        == test_item_id
                    ]


                    if len(rows) == 0:

                        continue


                    test_rows.append(
                        rows.iloc[0]
                    )


                # =================================================
                # Count Required
                # =================================================

                required_count = 0


                for row in test_rows:

                    applicability = str(
                        row["applicability"]
                    ).strip().upper()


                    if applicability == "REQUIRED":

                        required_count += 1


                # =================================================
                # Standard Header
                # =================================================

                st.markdown(
                    f'<div class="standard-header">'
                    f'{standard_code}'
                    f'</div>',
                    unsafe_allow_html=True,
                )


                st.markdown(
                    f'<span class="result-count">'
                    f'{len(test_rows)} 個測試項目'
                    f'　|　'
                    f'Required: {required_count}'
                    f'</span>',
                    unsafe_allow_html=True,
                )


                # =================================================
                # Test Item Table
                # =================================================

                table_parts = []


                table_parts.append(
                    '<table class="compliance-table">'
                )

                table_parts.append(
                    '<thead>'
                    '<tr>'
                    '<th style="width:32%;">測試項目</th>'
                    '<th style="width:18%;">測試類型</th>'
                    '<th style="width:18%;">適用性</th>'
                    '<th>說明</th>'
                    '</tr>'
                    '</thead>'
                )

                table_parts.append(
                    '<tbody>'
                )


                for row in test_rows:

                    test_name = str(
                        row["test_item_name"]
                    )

                    test_type = str(
                        row["test_type"]
                    )

                    applicability = str(
                        row["applicability"]
                    ).strip()

                    description = str(
                        row["description"]
                    )


                    if (
                        applicability.upper()
                        == "REQUIRED"
                    ):

                        badge = (
                            '<span class="required-badge">'
                            'Required'
                            '</span>'
                        )

                    else:

                        badge = (
                            '<span class="optional-badge">'
                            f'{applicability}'
                            '</span>'
                        )


                    table_parts.append(
                        '<tr>'
                        f'<td><strong>{test_name}</strong></td>'
                        f'<td>{test_type}</td>'
                        f'<td>{badge}</td>'
                        f'<td>{description}</td>'
                        '</tr>'
                    )


                table_parts.append(
                    '</tbody>'
                )

                table_parts.append(
                    '</table>'
                )


                st.markdown(
                    "".join(table_parts),
                    unsafe_allow_html=True,
                )


                # =================================================
                # Standard Details
                # =================================================

                with st.expander(
                    f"查看 {standard_code} 詳細資料"
                ):

                    detail_col1, detail_col2 = (
                        st.columns(2)
                    )


                    with detail_col1:

                        st.markdown(
                            f"**Standard ID**  \n"
                            f"{standard_id}"
                        )

                        st.markdown(
                            f"**Standard Code**  \n"
                            f"{standard_code}"
                        )

                        st.markdown(
                            f"**Version**  \n"
                            f"{standard['version']}"
                        )


                    with detail_col2:

                        st.markdown(
                            f"**Status**  \n"
                            f"{standard['status']}"
                        )

                        st.markdown(
                            f"**Effective Date**  \n"
                            f"{standard['effective_date']}"
                        )

                        st.markdown(
                            f"**Last Reviewed**  \n"
                            f"{standard['last_reviewed']}"
                        )


                    st.markdown(
                        f"**Standard Name**  \n"
                        f"{standard_name}"
                    )


                    st.markdown(
                        f"**Description**  \n"
                        f"{standard['description']}"
                    )


                    st.divider()


                    st.markdown(
                        "#### 測試項目詳細資料"
                    )


                    # ---------------------------------------------
                    # Individual Test Item
                    # ---------------------------------------------

                    for row in test_rows:

                        test_name = str(
                            row["test_item_name"]
                        )


                        with st.expander(
                            test_name
                        ):

                            col1, col2 = (
                                st.columns(2)
                            )


                            with col1:

                                st.write(
                                    "**Test Item ID**"
                                )

                                st.write(
                                    row["test_item_id"]
                                )


                                st.write(
                                    "**Category**"
                                )

                                st.write(
                                    row["test_category"]
                                )


                                st.write(
                                    "**Test Type**"
                                )

                                st.write(
                                    row["test_type"]
                                )


                            with col2:

                                st.write(
                                    "**Applicability**"
                                )

                                st.write(
                                    row["applicability"]
                                )


                                st.write(
                                    "**Last Reviewed**"
                                )

                                st.write(
                                    row["last_reviewed"]
                                )


                            st.write(
                                "**Description**"
                            )

                            st.write(
                                row["description"]
                            )


# =========================================================
# System Information
# =========================================================

with st.expander(
    "系統資訊"
):

    st.write(
        "本頁負責產品條件輸入與法規適用性判定。"
    )

    st.write(
        "判定流程："
        "Product Condition → "
        "Rule Engine → "
        "Regulation → "
        "Standard → "
        "Test Item"
    )
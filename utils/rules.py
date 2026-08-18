import pandas as pd

from utils.database import load_rules


# =========================================================
# Check Single Condition
# =========================================================

def check_condition(
    product,
    condition_type,
    condition_operator,
    condition_value,
):

    product_value = product.get(
        condition_type,
        "",
    )

    condition_value = str(
        condition_value
    ).strip()

    # -----------------------------------------------------
    # Normalize Boolean
    # -----------------------------------------------------

    if isinstance(product_value, bool):

        condition_value_lower = (
            condition_value.lower()
        )

        if condition_value_lower in [
            "true",
            "yes",
            "1",
        ]:

            condition_value = True

        elif condition_value_lower in [
            "false",
            "no",
            "0",
        ]:

            condition_value = False


    # -----------------------------------------------------
    # EQUAL
    # -----------------------------------------------------

    if condition_operator == "EQUAL":

        if isinstance(product_value, bool):

            return (
                product_value
                == condition_value
            )

        return (
            str(product_value).strip()
            == str(condition_value).strip()
        )


    # -----------------------------------------------------
    # NOT_EQUAL
    # -----------------------------------------------------

    if condition_operator == "NOT_EQUAL":

        if isinstance(product_value, bool):

            return (
                product_value
                != condition_value
            )

        return (
            str(product_value).strip()
            != str(condition_value).strip()
        )


    # -----------------------------------------------------
    # CONTAINS
    # -----------------------------------------------------

    if condition_operator == "CONTAINS":

        return (
            str(condition_value)
            in str(product_value)
        )


    # -----------------------------------------------------
    # EXISTS
    # -----------------------------------------------------

    if condition_operator == "EXISTS":

        if isinstance(product_value, bool):

            return product_value

        return (
            str(product_value).strip() != ""
            and str(product_value).lower()
            not in [
                "no",
                "none",
                "false",
            ]
        )


    # -----------------------------------------------------
    # Default
    # -----------------------------------------------------

    return False


# =========================================================
# Evaluate Rule Conditions
# =========================================================

def evaluate_rule_conditions(
    product,
    rule_rows,
):

    # -----------------------------------------------------
    # Old Format
    #
    # 如果沒有 condition_logic，
    # 就維持原本單一條件判斷方式。
    # -----------------------------------------------------

    if "condition_logic" not in rule_rows.columns:

        row = rule_rows.iloc[0]

        return check_condition(
            product,
            row["condition_type"],
            row["condition_operator"],
            row["condition_value"],
        )


    # -----------------------------------------------------
    # New Format
    #
    # 同一個 Rule ID 可以有多個 Condition。
    #
    # condition_logic:
    #
    # OR
    # → 任一條件成立即可
    #
    # AND
    # → 所有條件都成立
    # -----------------------------------------------------

    conditions = []


    for _, row in rule_rows.iterrows():

        matched = check_condition(
            product,
            row["condition_type"],
            row["condition_operator"],
            row["condition_value"],
        )

        conditions.append(
            matched
        )


    # -----------------------------------------------------
    # Determine Logic
    # -----------------------------------------------------

    logic_values = (
        rule_rows["condition_logic"]
        .fillna("OR")
        .astype(str)
        .str.upper()
        .tolist()
    )


    # -----------------------------------------------------
    # AND
    # -----------------------------------------------------

    if "AND" in logic_values:

        return all(
            conditions
        )


    # -----------------------------------------------------
    # Default OR
    # -----------------------------------------------------

    return any(
        conditions
    )


# =========================================================
# Evaluate Product
# =========================================================

def evaluate_product(
    product,
):

    rules = load_rules()

    # =====================================================
    # Filter by Market
    # =====================================================

    market = str(
        product.get("MARKET", "")
    ).strip().upper()

    if "market" in rules.columns:

        rules = rules[
            rules["market"]
            .fillna("")
            .astype(str)
            .str.strip()
            .str.upper()
            .isin(["", market])
        ].copy()

    results = []


    # =====================================================
    # Sort by Priority
    # =====================================================

    if "priority" in rules.columns:

        rules["priority"] = pd.to_numeric(
            rules["priority"],
            errors="coerce",
        ).fillna(999)

        rules = rules.sort_values(
            "priority"
        )


    # =====================================================
    # Group Rules
    # =====================================================

    grouped_rules = rules.groupby(
        "rule_id",
        sort=False,
    )


    # =====================================================
    # Evaluate Each Rule
    # =====================================================

    for rule_id, rule_rows in grouped_rules:

        # -------------------------------------------------
        # Check Rule Status
        # -------------------------------------------------

        if "status" in rule_rows.columns:

            status = str(
                rule_rows.iloc[0]["status"]
            ).strip().upper()

            if status not in [
                "ACTIVE",
                "",
                "NAN",
            ]:

                continue


        # -------------------------------------------------
        # Evaluate Conditions
        # -------------------------------------------------

        matched = evaluate_rule_conditions(
            product,
            rule_rows,
        )


        if not matched:

            continue


        # -------------------------------------------------
        # Use First Row as Rule Metadata
        # -------------------------------------------------

        rule = rule_rows.iloc[0]


        # -------------------------------------------------
        # Create Result
        # -------------------------------------------------

        results.append(
            {
                "rule_id":
                    rule["rule_id"],

                "regulation_id":
                    rule["regulation_id"],

                "standard_id":
                    rule["standard_id"],

                "test_item_id":
                    rule["test_item_id"],

                "result":
                    rule["result"],

                "reason":
                    rule["reason"],

                "priority":
                    rule["priority"],

                "source_id":
                    rule.get(
                        "source_id",
                        "",
                    ),

                "rule_version":
                    rule.get(
                        "rule_version",
                        "",
                    ),
            }
        )


    return results
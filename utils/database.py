from pathlib import Path
import pandas as pd


# ==========================================
# Project Path
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"


# ==========================================
# CSV Files
# ==========================================

REGULATIONS_FILE = DATA_DIR / "regulations.csv"

STANDARDS_FILE = DATA_DIR / "standards.csv"

TEST_ITEMS_FILE = DATA_DIR / "test_items.csv"

RULES_FILE = DATA_DIR / "rules.csv"

SOURCES_FILE = DATA_DIR / "sources.csv"


# ==========================================
# Load Regulations
# ==========================================

def load_regulations():

    return pd.read_csv(
        REGULATIONS_FILE,
        dtype=str
    ).fillna("")


# ==========================================
# Load Standards
# ==========================================

def load_standards():

    return pd.read_csv(
        STANDARDS_FILE,
        dtype=str
    ).fillna("")


# ==========================================
# Load Test Items
# ==========================================

def load_test_items():

    return pd.read_csv(
        TEST_ITEMS_FILE,
        dtype=str
    ).fillna("")


# ==========================================
# Load Rules
# ==========================================

def load_rules():

    return pd.read_csv(
        RULES_FILE,
        dtype=str
    ).fillna("")


# ==========================================
# Load Sources
# ==========================================

def load_sources():

    return pd.read_csv(
        SOURCES_FILE,
        dtype=str
    ).fillna("")


# ==========================================
# Load All Data
# ==========================================

def load_all_data():

    return {

        "regulations":
            load_regulations(),

        "standards":
            load_standards(),

        "test_items":
            load_test_items(),

        "rules":
            load_rules(),

        "sources":
            load_sources()
    }
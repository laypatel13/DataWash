import pandas as pd
import numpy as np
import pytest
from modules.cleaner import clean_csv
import os

# Create a temporary messy CSV for testing
@pytest.fixture
def messy_csv(tmp_path):
    data = {
        "name": ["Alice", "Bob", "Alice", "Charlie", None],
        "age": [25, 30, 25, None, 999],
        "salary": [50000, 60000, 50000, 75000, None],
        "department": ["Engineering", "Marketing", "Engineering", None, "Sales"]
    }
    df = pd.DataFrame(data)
    filepath = tmp_path / "test.csv"
    df.to_csv(filepath, index=False)
    return str(filepath)

# Test 1 — cleaner returns a dataframe
def test_clean_returns_dataframe(messy_csv):
    df, report = clean_csv(messy_csv)
    assert isinstance(df, pd.DataFrame)

# Test 2 — duplicates are removed
def test_duplicates_removed(messy_csv):
    df, report = clean_csv(messy_csv)
    assert report["duplicates_removed"] >= 1

# Test 3 — no missing values after cleaning
def test_no_missing_values(messy_csv):
    df, report = clean_csv(messy_csv)
    assert df.isnull().sum().sum() == 0

# Test 4 — report has all expected keys
def test_report_keys(messy_csv):
    df, report = clean_csv(messy_csv)
    keys = ["original_rows", "duplicates_removed", "missing_values_fixed",
            "outliers_removed", "cleaned_rows"]
    for key in keys:
        assert key in report

# Test 5 — cleaned rows less than or equal to original
def test_cleaned_rows_lte_original(messy_csv):
    df, report = clean_csv(messy_csv)
    assert report["cleaned_rows"] <= report["original_rows"]
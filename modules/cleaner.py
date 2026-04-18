import pandas as pd
import numpy as np

def clean_csv(filepath):
    df = pd.read_csv(filepath)
    report = {}

    # 1. Original shape 
    report["original_rows"] = len(df)
    report["original_cols"] = len(df.columns)

    # 2. Remove duplicate rows
    duplicates = df.duplicated().sum()
    df = df.drop_duplicates()
    report["duplicates_removed"] = int(duplicates)

    # 3. Fix missing values 
    missing_before = df.isnull().sum().sum()
    for col in df.columns:
        if df[col].dtype in ["float64", "int64"]:
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else "Unknown")
    report["missing_values_fixed"] = int(missing_before)

    # 4. Fix data types 
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except (ValueError, TypeError):
            pass
    
    # 5. Remove outliers (numeric columns only)
    outliers_removed = 0
    for col in df.select_dtypes(include=[np.number]).columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        before = len(df)
        df = df[~((df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR)))]
        outliers_removed += before - len(df)
    report["outliers_removed"] = int(outliers_removed)

    # 6. Final shape 
    report["cleaned_rows"] = len(df)
    report["cleaned_cols"] = len(df.columns)

    return df, report
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analyze_csv(df, upload_folder):
    report = {}
    charts = []

    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    text_cols = df.select_dtypes(exclude=[np.number]).columns.tolist()

    # 1. Basic stats
    report["total_rows"] = len(df)
    report["total_cols"] = len(df.columns)
    report["numeric_cols"] = len(numeric_cols)
    report["text_cols"] = len(text_cols)
    report["stats"] = df.describe().round(2).to_dict()

    charts_folder = os.path.join("static", "charts")
    os.makedirs(charts_folder, exist_ok=True)

    # 2. Histogram for each numeric column
    for col in numeric_cols:
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.histplot(df[col], kde=True, ax=ax, color="#0077b6")
        ax.set_title(f"Distribution of {col}")
        ax.set_facecolor("#0f0f1a")
        fig.patch.set_facecolor("#0f0f1a")
        ax.tick_params(colors="white")
        ax.title.set_color("white")
        ax.xaxis.label.set_color("white")
        ax.yaxis.label.set_color("white")
        fname = f"hist_{col}.png"
        fig.savefig(os.path.join(charts_folder, fname), bbox_inches="tight")
        plt.close()
        charts.append(fname)

    # 3. Correlation heatmap
    if len(numeric_cols) >= 2:
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(df[numeric_cols].corr().round(2), annot=True,
                    cmap="Blues", ax=ax)
        ax.set_title("Correlation Heatmap", color="white")
        ax.set_facecolor("#0f0f1a")
        fig.patch.set_facecolor("#0f0f1a")
        ax.tick_params(colors="white")
        fname = "heatmap.png"
        fig.savefig(os.path.join(charts_folder, fname), bbox_inches="tight")
        plt.close()
        charts.append(fname)

    # 4. Bar chart for text columns
    for col in text_cols[:2]:
        fig, ax = plt.subplots(figsize=(6, 4))
        df[col].value_counts().plot(kind="bar", ax=ax, color="#0077b6")
        ax.set_title(f"Value Counts: {col}", color="white")
        ax.set_facecolor("#0f0f1a")
        fig.patch.set_facecolor("#0f0f1a")
        ax.tick_params(colors="white")
        ax.xaxis.label.set_color("white")
        ax.yaxis.label.set_color("white")
        fname = f"bar_{col}.png"
        fig.savefig(os.path.join(charts_folder, fname), bbox_inches="tight")
        plt.close()
        charts.append(fname)

    return report, charts
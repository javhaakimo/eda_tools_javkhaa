import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def basic_stats(x):
    """Тоон массивын үндсэн статистик."""
    x = np.array(x)

    return {
        "n": len(x),
        "mean": round(float(x.mean()), 2),
        "median": float(np.median(x)),
        "std": round(float(x.std(ddof=1)), 2),
        "min": float(x.min()),
        "max": float(x.max())
    }


def iqr_outliers(x):
    """1.5 x IQR дүрмээр outlier утгуудыг буцаана."""
    x = np.array(x)

    q1, q3 = np.percentile(x, [25, 75])
    iqr = q3 - q1

    return x[
        (x < q1 - 1.5 * iqr) |
        (x > q3 + 1.5 * iqr)
    ]


def missing_report(df):
    """Багана бүрийн хоосон утгын тоо ба хувь."""
    n = df.isnull().sum()

    return pd.DataFrame({
        "missing": n,
        "percent": (n / len(df) * 100).round(1)
    })


def group_rate(df, by, target):
    """Бүлэг бүрийн хүний тоо ба target-ийн дундаж."""
    return (
        df.groupby(by)[target]
        .agg(["count", "mean"])
        .round(2)
    )


def plot_hist(df, col):
    """Histogram, дундаж ба медианы шугамтай."""
    fig, ax = plt.subplots(figsize=(7, 4))

    ax.hist(df[col], bins=30, edgecolor="white")

    ax.axvline(
        df[col].mean(),
        color="orange",
        lw=4,
        label=f"дундаж = {df[col].mean():.1f}"
    )

    ax.axvline(
        df[col].median(),
        color="red",
        lw=2,
        ls="--",
        label=f"медиан = {df[col].median():.1f}"
    )

    ax.set_title(col)
    ax.legend()
    plt.show()


def plot_box(df, x, y):
    """Бүлэг бүрийн тархалтыг boxplot-оор харьцуулна."""
    sns.boxplot(data=df, x=x, y=y)
    plt.title(f"{y} ба {x}")
    plt.show()


def plot_corr(df):
    """Тоон багануудын корреляцийн heatmap."""
    corr = df.select_dtypes("number").corr()

    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        vmin=-1,
        vmax=1
    )

    plt.title("Корреляц")
    plt.show()
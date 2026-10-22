
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path


def plot_hist(df, col, path=None):
    """Histogram, дундаж болон медианы шугамтай."""

    fig, ax = plt.subplots(figsize=(7, 4))

    ax.hist(df[col].dropna(), bins=30, edgecolor="white")

    ax.axvline(
        df[col].mean(),
        color="orange",
        lw=4,
        label=f"Дундаж = {df[col].mean():.1f}"
    )

    ax.axvline(
        df[col].median(),
        color="red",
        lw=2,
        ls="--",
        label=f"Медиан = {df[col].median():.1f}"
    )

    ax.set_title(col)
    ax.legend()

    _finish(fig, path)


def plot_box(df, x, y, path=None):
    """Бүлгүүдийн тархалтыг boxplot-оор харьцуулна."""

    fig, ax = plt.subplots(figsize=(7, 4))

    sns.boxplot(data=df, x=x, y=y, ax=ax)

    ax.set_title(f"{y} ба {x}")

    _finish(fig, path)


def plot_corr(df, path=None):
    """Тоон багануудын корреляцийн heatmap."""

    corr = df.select_dtypes(include="number").corr()

    fig, ax = plt.subplots(figsize=(7, 5))

    sns.heatmap(
        corr,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        vmin=-1,
        vmax=1,
        ax=ax
    )

    ax.set_title("Корреляц")

    _finish(fig, path)


def _finish(fig, path=None):
    """Графикийг харуулах эсвэл файл болгон хадгалах."""

    fig.tight_layout()

    if path is not None:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(path, dpi=150, bbox_inches="tight")

    plt.show()
    plt.close(fig)

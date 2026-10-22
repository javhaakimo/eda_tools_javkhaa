
import numpy as np


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


def group_rate(df, by, target):
    """Бүлэг бүрийн тоо болон target-ийн дундаж."""

    return (
        df.groupby(by)[target]
        .agg(["count", "mean"])
        .round(2)
    )

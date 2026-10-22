
import numpy as np
import pandas as pd


def missing_report(df):
    """Багана бүрийн хоосон утгын тоо болон хувийг тооцно."""

    n = df.isnull().sum()

    return pd.DataFrame({
        "missing": n,
        "percent": (n / len(df) * 100).round(1)
    })


def iqr_outliers(x):
    """IQR аргаар хэт ялгаатай утгуудыг илрүүлнэ."""

    x = np.array(x)

    q1, q3 = np.percentile(x, [25, 75])
    iqr = q3 - q1

    return x[
        (x < q1 - 1.5 * iqr) |
        (x > q3 + 1.5 * iqr)
    ]

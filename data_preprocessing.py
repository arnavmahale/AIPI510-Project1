import os
import numpy
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression, RidgeCV, LassoCV
from sklearn.metrics import mean_absolute_error, r2_score
from pathlib import Path
path = Path()

filepath: Path = f"{path}/insurance.csv"

def load_data(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    df_fe = df.copy()

    # add a column for "obesity"
    df_fe["obese"] = (df_fe["bmi"] >= 30).astype(int) # 1: obese, 0: not obese

    # age buckets
    AGE_BINS = [0, 30, 45, 60, 200]
    AGE_LABELS = ["18-30", "31-45", "46-60", "61+"]
    df_fe["age_group"] = pd.cut(df_fe["age"], bins=AGE_BINS, labels=AGE_LABELS, right=True, include_lowest=True)

    return df_fe

def main():
    # load the data
    df = load_data(filepath)

    # feature engineering
    df_fe = engineer_features(df)

    df_fe.to_csv('insurance_fe.csv', index=False)

if __name__ == "__main__":
    main()
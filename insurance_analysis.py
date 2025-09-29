#  Libraries 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

#  Load Data 
df = pd.read_csv("insurance.csv")

#  Exploratory Data Analysis (EDA) 
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Distribution plots
sns.histplot(df['age'], bins=20, kde=True)
plt.title("Age Distribution")
plt.show()

sns.histplot(df['bmi'], bins=20, kde=True)
plt.title("BMI Distribution")
plt.show()

sns.boxplot(x='smoker', y='charges', data=df)
plt.title("Charges vs Smoker Status")
plt.show()

sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

#  Preprocessing / Feature Engineering 
# Separate features and target
X = df.drop("charges", axis=1)
y = df["charges"]

# Categorical and numeric columns
categorical = ["sex", "smoker", "region"]
numeric = ["age", "bmi", "children"]

# Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric),
        ("cat", OneHotEncoder(drop="first"), categorical)
    ]
)

#  Modeling 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

#  Evaluation 
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R2:", r2_score(y_test, y_pred))

# Important notes on ethical considerations
print("\nEthical Considerations:")
print("- Dataset may underrepresent certain regions or demographics.")
print("- Charges reflect systemic healthcare cost inequities.")
print("- Features like 'smoker' may reinforce stigma if misused.")
print("- Always consider fairness when applying models to policy or pricing.")

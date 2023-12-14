import pandas as pd
from sklearn.linear_model import LinearRegression

csv = "2023-2024stats.csv"
data = pd.read_csv(csv)

data.head()
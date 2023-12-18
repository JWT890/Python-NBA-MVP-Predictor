import pandas as pd
from sklearn.linear_model import LinearRegression

csv = "2017-2018stats.csv"
data = pd.read_csv(csv)

data.head()
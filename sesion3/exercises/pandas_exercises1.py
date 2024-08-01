import pandas as pd

# Load data from biostats.csv file.
df = pd.read_csv("biostats.csv")

# Delete rows with any inexistant entry (NaN).
df = df.dropna()
print(df)


mean_weight = df[df["Sex"] == "M"]["Weight"].mean()


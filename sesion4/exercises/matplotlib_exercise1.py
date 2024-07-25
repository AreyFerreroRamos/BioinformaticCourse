import pandas as pd
import matplotlib.pyplot as plt

def calculate_imc(df):
    df["imc"] = df["Weight"] / (df["Height"] * df["Height"])
    return df

if __name__ == "__main__":
    
    df_biostats = pd.read_csv("biostats.csv")

    df_biostats = df_biostats.dropna()

    df_imc = calculate_imc(df_biostats)
    print(df_imc)

    grouped_df_imc = df_imc.groupby("Sex")
    df_mean_imc = grouped_df_imc.agg(Mean_imc=("imc", "mean"))
    print(df_mean_imc)

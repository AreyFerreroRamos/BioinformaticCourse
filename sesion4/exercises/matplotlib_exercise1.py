import matplotlib.pyplot as plt
import pandas as pd
import sys

def calculate_imc(df):
    df["Imc"] = df["Weight"] / (df["Height"] * df["Height"])
    return df

if __name__ == "__main__":
    df_biostats = pd.read_csv(sys.argv[1])
    df_biostats = df_biostats.dropna()
    print(df_biostats)

    df_imc = calculate_imc(df_biostats)
    print(df_imc)

    grouped_df_imc = df_imc.groupby("Sex")
    df_mean_imc = grouped_df_imc.agg(Mean_imc=("Imc", "mean"))
    print(df_mean_imc)

    df_mean_imc = df_mean_imc.reset_index()
    print(df_mean_imc)

    plt.bar(x=df_mean_imc["Sex"], height=df_mean_imc["Mean_imc"])
    plt.show()
    
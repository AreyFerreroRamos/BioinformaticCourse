import matplotlib.pyplot as plt
import pandas as pd
import sys


def calculate_imc(df):
    df["Imc"] = df["Weight"] / (df["Height"] * df["Height"])
    return df


if __name__ == "__main__":
    # Load data from 'biostats.csv' file and delete rows with any inexistant entry (NaN).
    df_biostats = pd.read_csv(sys.argv[1])
    df_biostats = df_biostats.dropna()
    print(df_biostats)

    # Calculate the IMC mean in men and women (separately).
    df_imc = calculate_imc(df_biostats)
    print(df_imc)

    grouped_df_imc = df_imc.groupby("Sex")
    df_mean_imc = grouped_df_imc.agg(Mean_imc=("Imc", "mean"))
    print(df_mean_imc)

    df_mean_imc = df_mean_imc.reset_index()
    print(df_mean_imc)

    # Represent the IMC means in a bar plot.
    plt.bar(x=df_mean_imc["Sex"], height=df_mean_imc["Mean_imc"])
    plt.show()
    
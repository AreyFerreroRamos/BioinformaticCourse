import pandas as pd
import sys


def calculate_imc(df):
    df["IMC"] = df["Weight"] / (df["Height"] * df["Height"])
    return df


if __name__ == "__main__":
    # Load data from biostats file.
    df = pd.read_csv(sys.argv[1])
    print(df)

    # Delete rows with any inexistant entry (NaN).
    df = df.dropna()
    print(df)

    # Calculate the IMC of each individual.
    print(calculate_imc(df))

    # Calculate the mean weight in men.
    mean_weight_men = df[df["Sex"] == "M"]["Weight"].mean()
    print(mean_weight_men)

    # Calculate standard desviation in height in women greater than 35 years. 
    # The standard desviation is NaN beacuse there is only one element.
    std_desv_height = df[(df["Sex"] == "F") & (df["Age"] > 35)]["Height"].std()
    print(std_desv_height)

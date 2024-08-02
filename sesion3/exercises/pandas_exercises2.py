import pandas as pd
import sys


def young_or_old(x):
    if (x > 32):
        return "old"
    else:
        return "young"

 
if __name__ == "__main__":
    # Load data from mammal life file.
    df_mammal_life = pd.read_csv(sys.argv[1])
    print(df_mammal_life)

    # FIlter the species whose gestation lifetime is not recorded (negative values)
    # and group by its order.
    grouped_df = df_mammal_life[df_mammal_life["gestation(mo)"] >= 0].groupby("order")
    print(grouped_df)

    # Calculate the mean of gestation time in the species that pertains to the same order.
    df_means = grouped_df.mean("gestation(mo)")
    print(df_means)


    # Load data from biostats file.
    df_biostats = pd.read_csv(sys.argv[2])
    print(df_biostats)

    # Delete rows with any inexistant entry (NaN).
    df_biostats = df_biostats.dropna()

    # Calculate the mean of the height grouped by sex.
    grouped_df = df_biostats[["Sex", "Height"]].groupby("Sex")
    mean_df = grouped_df.mean("Height").rename(columns={"Height": "Mean_height"})
    print(mean_df)

    # Calculate the mean and the standard desviation of the height grouped by sex using an aggregation.
    grouped_df = df_biostats[["Sex", "Height"]].groupby("Sex")
    mean_df = grouped_df.agg(Mean=("Height", "mean"), Std_desviation=("Height", "std"))
    print(mean_df)

    grouped_df = df_mammal_life[["order", "gestation(mo)"]].groupby("order")
        
    df_modified = df_biostats.assign(oldness=df_biostats["Age"].apply(young_or_old))
    grouped_df = df_modified[["Sex", "oldness", "Height"]].groupby(["Sex"])
    mean_df = grouped_df.agg(Mean=("Height", "mean"), Std_desviation=("Height", "std"))
    print(mean_df)

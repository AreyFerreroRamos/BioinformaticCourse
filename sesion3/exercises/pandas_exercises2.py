import pandas as pd


def young_or_old(x):
    if (x > 32):
        return "old"
    else:
        return "young"

 
if __name__ == "__main__":
    df_biostats = pd.read_csv("biostats.csv")
    print(df_biostats)
    
    df_mammal_life = pd.read_csv("mammal_life.csv")
    print(df_mammal_life)

    df_biostats = df_biostats.dropna()

    grouped_df = df_mammal_life.groupby("order")
    print(grouped_df)

    df_means = grouped_df.mean("gestation(mo)")
    print(df_means)

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

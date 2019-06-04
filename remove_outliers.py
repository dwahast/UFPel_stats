
import pandas as pd
from typing import List

def remove_outliers(dataframe: pd.DataFrame, columns_to_remove:List[str]):
    df = dataframe
    df_outliers = dataframe[columns_to_remove]
    desc = df_outliers.describe()

    Q3 = desc.iloc[6,:]
    Q1 = desc.iloc[4,:]
    aq = Q3 - Q1
    desloc = 1.5 * aq

    sup_lim = Q3 + desloc
    inf_lim = Q1 - desloc

    numerical_columns = desc.columns

    outliers = {}
    for c in numerical_columns:
        outliers[c] = df[(df[str(c)] > sup_lim[c]) | (df[c] < inf_lim[c])][c].count()

    outliers_count = 0
    for c in numerical_columns:
        outliers_count += outliers[c]

    print("outliers number: {}\n".format(outliers_count))
    
    if(outliers_count==0):
        return df

    for c in numerical_columns:
        df = df[(df[c] <= sup_lim[c]) & (df[c] >= inf_lim[c])]

    return remove_outliers(df, columns_to_remove)

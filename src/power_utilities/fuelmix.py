import pandas as pd
import numpy as np
import datetime
import glob

from power_utilities.NamedLists import column_list_Mwh, column_list_power


class Fuelmix:

    def __init__(self, region):
        self.region = region

    def utility_fuelmix(self):
        dfwhole = pd.DataFrame()
        filenames = glob.glob('../dataset/' + self.region + '2020/*.csv')
        print(filenames)
        # filenames.sort()
        for a in filenames:
            print(a)
            temp = pd.read_csv(a)
            # temp.rename(columns=temp.iloc[0], inplace = True)
            format = '%Y-%m-%d %H:%M:%S'
            temp['Timestamp'] = pd.to_datetime(temp['Timestamp (Hour Ending)'], format=format, errors='ignore')
            for col in column_list_Mwh:
                if col not in temp.columns:
                    temp[col] = 0
            temp["total Generation (MWh)"] = temp[np.array(column_list_Mwh)].sum(axis=1)
            dfwhole = dfwhole.append(temp)

        dfwhole = dfwhole.reset_index(drop=True)
        dfwhole["Wind Generation (%)"] = dfwhole["Wind Generation (MWh)"] * 100 / dfwhole["total Generation (MWh)"]
        dfwhole["Solar Generation (%)"] = dfwhole["Solar Generation (MWh)"] * 100 / dfwhole["total Generation (MWh)"]
        dfwhole["Hydro Generation (%)"] = dfwhole["Hydro Generation (MWh)"] * 100 / dfwhole["total Generation (MWh)"]
        dfwhole["Other Generation (%)"] = dfwhole["Other Generation (MWh)"] * 100 / dfwhole["total Generation (MWh)"]
        dfwhole["Petroleum Generation (%)"] = dfwhole["Petroleum Generation (MWh)"] * 100 / dfwhole[
            "total Generation (MWh)"]
        dfwhole["Natural gas Generation (%)"] = dfwhole["Natural gas Generation (MWh)"] * 100 / dfwhole[
            "total Generation (MWh)"]
        dfwhole["Coal Generation (%)"] = dfwhole["Coal Generation (MWh)"] * 100 / dfwhole["total Generation (MWh)"]
        dfwhole["Nuclear Generation (%)"] = dfwhole["Nuclear Generation (MWh)"] * 100 / dfwhole[
            "total Generation (MWh)"]
        dfwhole["Battery Generation (%)"] = dfwhole["Battery Generation (MWh)"] * 100 / dfwhole[
            "total Generation (MWh)"]
        dfwhole["Imports Generation (%)"] = dfwhole["Imports Generation (MWh)"] * 100 / dfwhole[
            "total Generation (MWh)"]

        return dfwhole

    def calculate_fuelmixbypercent(self, df):
        if not df["power(W)"].any():
            print("No power found")
        else:
            print(df.head())

        dfpercent = self.utility_fuelmix()
        if not dfpercent["Wind Generation (%)"].any():
            print("No dfpercent found")
        else:
            print(dfpercent.head())

        # df_percent_fuelmix = df_percent_fuelmix.reset_index(drop=True)
        # if dfnw["Timestamp (Hour Ending)"].Hour == dfwhole1["Timestamp"].Hour :
        df["Wind(W)"] = dfpercent["Wind Generation (%)"] * df["power(W)"] / 100
        df["Solar(W)"] = dfpercent["Solar Generation (%)"] * df["power(W)"] / 100
        df["Hydro(W)"] = dfpercent["Hydro Generation (%)"] * df["power(W)"] / 100
        df["Other(W)"] = dfpercent["Other Generation (%)"] * df["power(W)"] / 100
        df["Petroleum(W)"] = dfpercent["Petroleum Generation (%)"] * df["power(W)"] / 100
        df["Natural gas(W)"] = dfpercent["Natural gas Generation (%)"] * df["power(W)"] / 100
        df["Coal(W)"] = dfpercent["Coal Generation (%)"] * df["power(W)"] / 100
        df["Nuclear(W)"] = dfpercent["Nuclear Generation (%)"] * df["power(W)"] / 100
        df["Battery(W)"] = dfpercent["Battery Generation (%)"] * df["power(W)"] / 100
        df["Imports(W)"] = dfpercent["Imports Generation (%)"] * df["power(W)"] / 100

        df["total(W)"] = df[np.array(column_list_power)].sum(axis=1)
        return df

import pandas as pd
import numpy as np
import datetime
import os

from carbonfootprint.carbon import Carbon
from carbonfootprint.fuelmix import Fuelmix

class ManufacturingPlant_Carbonemission():

    def power_consumed(self):
        print(os.getcwd())
        print(__file__)
        dirname = os.path.dirname(__file__)
        dfindus = pd.read_csv(os.path.join(dirname, 'dataset/indust1data.csv'))
        dfindus.drop(["Unnamed: 4"], axis=1, inplace=True)
        dfindus.drop(["Unnamed: 5"], axis=1, inplace=True)
        dfindus.drop(["kvarh d"], axis=1, inplace=True)

        # print(dfindus.head())

        startdate = datetime.date(2009, 1, 1)
        enddate = datetime.date(2009, 12, 31)

        # nan and not null
        dfindus = dfindus[dfindus.Date.notnull()]

        dfindus["Date"] = pd.to_datetime(dfindus["Date"], errors='coerce').dt.date  # date
        dfindus["Time"] = pd.to_datetime(dfindus["Time"], errors='coerce').dt.time  # time

        # timesatmp format
        dfindus['Timestamp'] = pd.to_datetime(dfindus['Date'].apply(str) + ' ' + dfindus['Time'].apply(str),
                                              format='%Y-%m-%d %H:%M:%S')

        # Rename Columns
        dfindus = dfindus.rename(columns={"Date": "DATE",
                                          "Time": "TIME",
                                          "kWh d": "energy(kWh)"
                                          })
        # Remove duplicates
        dfindus = dfindus[dfindus['DATE'].between(startdate, enddate, inclusive=True)]
        dfindus = dfindus.sort_values(by=['Timestamp'], ascending=True)
        dfindus = dfindus.drop_duplicates(subset='Timestamp', keep="first")

        #  Fill undefined and nan
        dfindus = dfindus.replace('undefined', 0)
        dfindus = dfindus.fillna(0)
        dfindus = dfindus.replace(np.nan, 0)
        # dfindus = dfindus.set_index('TIME')
        # dfindus.index = dfindus['TIME']

        #  Power = Energy / Time
        dfindus["power(kW)"] = dfindus["energy(kWh)"] * 60 / 15
        dfindus["power(W)"] = dfindus["power(kW)"] * 1000

        dfindus_hourly = dfindus.resample('H', on='Timestamp').agg({
            'power(W)': 'mean',
            'Timestamp': 'first',
            'DATE': 'unique'})
        dfindus_hourly = dfindus_hourly.reset_index(drop=True)
        return dfindus_hourly

    def industry1_fuelmix_carbonemission(self):
        dfindus_hourly = self.power_consumed()
        furlpercent_obj = Fuelmix("north_west")
        dfindus_hourly_fuelmix = furlpercent_obj.calculate_fuelmixbypercent(dfindus_hourly)
        print("-------------dfindus_hourly_fuelmix------------------")
        print(dfindus_hourly_fuelmix.head())
        print(dfindus_hourly_fuelmix.columns)

        carbonemissio_pbj = Carbon()
        dfindus_hourly_fuelmix_carbon = carbonemissio_pbj.calculate_carbonemission(dfindus_hourly_fuelmix)
        print("-------------dfindus_hourly_fuelmix_carbon------------------")
        print(dfindus_hourly_fuelmix_carbon.head())
        print(dfindus_hourly_fuelmix_carbon.columns)


if __name__ == '__main__':
    ManufacturingPlant_Carbonemission.main()

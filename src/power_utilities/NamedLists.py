column_list = ("Wind", "Solar", "Hydro", "Other", "Petroleum", "Natural gas", "Coal", "Nuclear", "Battery", "Imports")

column_list_power = [sub + "(W)" for sub in column_list]

column_list_Mwh = ['Wind Generation (MWh)', 'Solar Generation (MWh)', 'Hydro Generation (MWh)',
                   'Other Generation (MWh)', 'Petroleum Generation (MWh)', 'Natural gas Generation (MWh)',
                   'Coal Generation (MWh)', 'Nuclear Generation (MWh)', 'Battery Generation (MWh)',
                   'Imports Generation (MWh)']

column_list_percent = [sub.replace("(MWh)", "(%)") for sub in column_list_Mwh]

column_list_carbon = ["carbon_" + sub + "(kgeCO2)" for sub in column_list]

import pandas as pd
oh_url = r'https://coronavirus.ohio.gov/static/COVIDSummaryData.csv'
df = pd.read_csv(oh_url)

df_county = df[['County','Case Count','Death Due to Illness Count','Hospitalized Count']]
df_county =df_county.replace('nan','0')
df_county['Case Count'] = df_county['Case Count'].str.replace(',','').astype(float)
df_county['Death Due to Illness Count'] = df_county['Death Due to Illness Count'].str.replace(',','').astype(float)
df_county['Hospitalized Count'] = df_county['Hospitalized Count'].str.replace(',','').astype(float)
df_county = df_county.set_index(['County']).sum()

print(df_county)
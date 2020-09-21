import pandas as pd
param = ""
oh_url = r'https://coronavirus.ohio.gov/static/COVIDSummaryData.csv'
df = pd.read_csv(oh_url,low_memory=False)
if param=="d":
    df_county = df[['County','Case Count','Death Due to Illness Count','Hospitalized Count','Onset Date']]
else:
    df_county = df[['County','Case Count','Death Due to Illness Count','Hospitalized Count']]
df_county['Case Count'] = df_county['Case Count'].str.replace(',','').astype(int)
df_county['Death Due to Illness Count'] = df_county['Death Due to Illness Count'].str.replace(',','').astype(int)
df_county['Hospitalized Count'] = df_county['Hospitalized Count'].str.replace(',','').astype(int)
if param =="d":
    d={}
    df_county = df_county.set_index(['Onset Date']).groupby(['County','Onset Date']).sum()
    counties = []
    dates=[]
    for i, rows in df_county.iterrows():
        counties.append(i[0])
        dates.append(i[1])
    county_list = []
    date_list = []
    for date in dates:
        if date not in date_list:
            date_list.append(date)
            d[date] ={}
    
    for i, rows in df_county.iterrows():
        date = i[1]
        county = i[0]
        d[date][county] = {}
    #print(d)
    for i, rows in df_county.iterrows():
        print(i[1])
        county = i[0]
        date = i[1]
        case_count = rows[0]
        death_count = rows[1]
        hosp_count = rows[2]
        d[date][county] = []
        d[county].append({"Case Count":case_count,"Death Due to Illness Count":death_count,"Hospitalized Count":hosp_count})
        
else:
    df_county = df_county.set_index(['County']).groupby(['County']).sum()
    d = df_county.to_dict()
print(d)
print(df_county.head(100))

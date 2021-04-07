from flask import Flask, request, render_template, jsonify
import pandas as pd

from flask_heroku import Heroku

#Code by James Labadorf. James@jameslabadorf.com
app = Flask(__name__)

heroku = Heroku(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sum/')
def summuraized():
    oh_url = r'https://coronavirus.ohio.gov/static/dashboards/COVIDDeathData_CountyOfResidence.csv'
    df = pd.read_csv(oh_url,low_memory=False)

    df_county = df[['County','Case Count','Death Due to Illness Count','Hospitalized Count']]
    df_county['Case Count'] = df_county['Case Count'].str.replace(',','').astype(int)
    df_county['Death Due to Illness Count'] = df_county['Death Due to Illness Count'].str.replace(',','').astype(int)
    df_county['Hospitalized Count'] = df_county['Hospitalized Count'].str.replace(',','').astype(int)
    df_county = df_county.set_index(['County']).sum()

    d = df_county.to_dict()
    return jsonify(d)


@app.route('/all/') # This pulls all the data from the ODH
def all_data():
    oh_url = r'https://coronavirus.ohio.gov/static/dashboards/COVIDDeathData_CountyOfResidence.csv'
    df = pd.read_csv(oh_url,low_memory=False)
    d  = df.to_dict()
    return jsonify(d)

@app.route('/county/')
def county_data():
    param = request.args.get("g")
    oh_url = r'https://coronavirus.ohio.gov/static/dashboards/COVIDDeathData_CountyOfResidence.csv'
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
    #print(df_county.head(100))
    return jsonify(d)
    
@app.route('/county/<county>/')
def county_lookup(county):
    oh_url = r'https://coronavirus.ohio.gov/static/dashboards/COVIDDeathData_CountyOfResidence.csv'
    df = pd.read_csv(oh_url,low_memory=False)
    df_county = df[['County','Case Count','Death Due to Illness Count','Hospitalized Count']]
    df_county['Case Count'] = df_county['Case Count'].str.replace(',','').astype(int)
    #df_county['Death Due to Illness Count'] = df_county['Death Due to Illness Count']#.str.replace(',','').astype(int)
    #df_county['Hospitalized Count'] = df_county['Hospitalized Count']#.str.replace(',','').astype(int)
    df_county = df_county.set_index(['County']).groupby(['County']).sum()
    d = df_county.loc[county].to_dict()
    return jsonify(d)

@app.route('/sex/')
def sex():
    oh_url = r'https://coronavirus.ohio.gov/static/dashboards/COVIDDeathData_CountyOfResidence.csv'
    df = pd.read_csv(oh_url,low_memory=False)
    df_county = df[['Sex','Case Count','Death Due to Illness Count','Hospitalized Count']]
    df_county['Case Count'] = df_county['Case Count'].str.replace(',','').astype(int)
   # df_county['Death Due to Illness Count'] = df_county['Death Due to Illness Count']#.str.replace(',','').astype(int)
   # df_county['Hospitalized Count'] = df_county['Hospitalized Count']#.str.replace(',','').astype(int)
    df_county = df_county.set_index(['Sex']).groupby(['County']).sum()
    d = df_county.to_dict()
    return jsonify(d)

@app.route('/onset/date/')
def onset_date():
    oh_url = r'https://coronavirus.ohio.gov/static/dashboards/COVIDDeathData_CountyOfResidence.csv'
    df = pd.read_csv(oh_url,low_memory=False)
    df_county = df[['Onset Date','Case Count','Death Due to Illness Count','Hospitalized Count']]
    df_county['Case Count'] = df_county['Case Count'].str.replace(',','').astype(int)
    #df_county['Death Due to Illness Count'] = df_county['Death Due to Illness Count']#.str.replace(',','').astype(int)
    #df_county['Hospitalized Count'] = df_county['Hospitalized Count']#.str.replace(',','').astype(int)
    df_county = df_county.set_index(['Onset Date']).groupby(['Onset Date']).sum()
    d = df_county.to_dict()
    return jsonify(d)

@app.route('/onset/date/<county>/')
def onset_date_county(county):
    oh_url = r'https://coronavirus.ohio.gov/static/dashboards/COVIDDeathData_CountyOfResidence.csv'
    df = pd.read_csv(oh_url,low_memory=False)
    df_county = df[['County','Onset Date','Case Count','Death Due to Illness Count','Hospitalized Count']]
    df_county['Case Count'] = df_county['Case Count'].str.replace(',','').astype(int)
    #df_county['Death Due to Illness Count'] = df_county['Death Due to Illness Count']#.str.replace(',','').astype(int)
    #df_county['Hospitalized Count'] = df_county['Hospitalized Count']#.str.replace(',','').astype(int)
    df_county = df_county.set_index(['County','Onset Date']).groupby(['County','Onset Date']).sum()
    d = df_county.loc[county].to_dict()
    return jsonify(d)

@app.route('/death/')
def death_count():
    oh_url = r'https://coronavirus.ohio.gov/static/dashboards/COVIDDeathData_CountyOfResidence.csv'
    df = pd.read_csv(oh_url,low_memory=False)
    df_county = df[['Date Of Death','Case Count','Death Due to Illness Count','Hospitalized Count']]
    df_county['Case Count'] = df_county['Case Count'].str.replace(',','').astype(int)
    #df_county['Death Due to Illness Count'] = df_county['Death Due to Illness Count']#.str.replace(',','').astype(int)
    #df_county['Hospitalized Count'] = df_county['Hospitalized Count']#.str.replace(',','').astype(int)
    df_county = df_county.set_index(['Date Of Death']).groupby(['Date Of Death']).sum()
    d = df_county.to_dict()
    return jsonify(d)

@app.route('/age/')
def age_group():
    oh_url = r'https://coronavirus.ohio.gov/static/dashboards/COVIDDeathData_CountyOfResidence.csv'
    df = pd.read_csv(oh_url,low_memory=False)
    df_county = df[['Age Range','Case Count','Death Due to Illness Count','Hospitalized Count']]
    df_county['Case Count'] = df_county['Case Count'].str.replace(',','').astype(int)
    #df_county['Death Due to Illness Count'] = df_county['Death Due to Illness Count'].str.replace(',','')#.astype(int)
    #df_county['Hospitalized Count'] = df_county['Hospitalized Count']#.str.replace(',','').astype(int)
    df_county = df_county.set_index(['Age Range']).groupby(['Age Range']).sum()
    d = df_county.to_dict()
    return jsonify(d)
if __name__ =='__main__':
    app.run()



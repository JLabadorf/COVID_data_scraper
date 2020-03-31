from flask import Flask, request, render_template, jsonify
import pandas as pd

from flask_heroku import Heroku

app = Flask(__name__)

heroku = Heroku(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/all/') # This pulls all the data from the ODH
def all_data():
    oh_url = r'https://coronavirus.ohio.gov/static/COVIDSummaryData.csv'
    df = pd.read_csv(oh_url)
    d  = df.to_dict()
    print(df.head(10))
    return jsonify(d)

@app.route('/county/')
def county_data():
    oh_url = r'https://coronavirus.ohio.gov/static/COVIDSummaryData.csv'
    df = pd.read_csv(oh_url)
    df_county = df[['County','Case Count','Death Count','Hospitalized Count']]
    df_county['Case Count'] = df_county['Case Count'].str.replace(',','').astype(int)
    #df_county['Death Count'] = df_county['Death Count'].str.replace(',','').astype(int)
    #df_county['Hospitalized Count'] = df_county['Hospitalized Count'].str.replace(',','').astype(int)
    df_county = df_county.set_index(['County']).groupby(['County']).sum()
    print(df_county.head(10))

    d = df_county.to_dict()
    return jsonify(d)
    
@app.route('/county/<county>/')
def county_lookup(county):
    oh_url = r'https://coronavirus.ohio.gov/static/COVIDSummaryData.csv'
    df = pd.read_csv(oh_url)
    df_county = df[['County','Case Count','Death Count','Hospitalized Count']]
    df_county['Case Count'] = df_county['Case Count'].str.replace(',','').astype(int)
    #df_county['Death Count'] = df_county['Death Count']#.str.replace(',','').astype(int)
    #df_county['Hospitalized Count'] = df_county['Hospitalized Count']#.str.replace(',','').astype(int)
    df_county = df_county.set_index(['County']).groupby(['County']).sum()
    d = df_county.loc[county].to_dict()
    return jsonify(d)

@app.route('/sex/')
def sex():
    oh_url = r'https://coronavirus.ohio.gov/static/COVIDSummaryData.csv'
    df = pd.read_csv(oh_url)
    df_county = df[['Sex','Case Count','Death Count','Hospitalized Count']]
    df_county['Case Count'] = df_county['Case Count'].str.replace(',','').astype(int)
   # df_county['Death Count'] = df_county['Death Count']#.str.replace(',','').astype(int)
   # df_county['Hospitalized Count'] = df_county['Hospitalized Count']#.str.replace(',','').astype(int)
    df_county = df_county.set_index(['Sex']).groupby(['County']).sum()
    d = df_county.to_dict()
    return jsonify(d)

@app.route('/onset/date/')
def onset_date():
    oh_url = r'https://coronavirus.ohio.gov/static/COVIDSummaryData.csv'
    df = pd.read_csv(oh_url)
    df_county = df[['Onset Date','Case Count','Death Count','Hospitalized Count']]
    df_county['Case Count'] = df_county['Case Count'].str.replace(',','').astype(int)
    #df_county['Death Count'] = df_county['Death Count']#.str.replace(',','').astype(int)
    #df_county['Hospitalized Count'] = df_county['Hospitalized Count']#.str.replace(',','').astype(int)
    df_county = df_county.set_index(['Onset Date']).groupby(['Onset Date']).sum()
    d = df_county.to_dict()
    return jsonify(d)

@app.route('/onset/date/<county>/')
def onset_date_county(county):
    oh_url = r'https://coronavirus.ohio.gov/static/COVIDSummaryData.csv'
    df = pd.read_csv(oh_url)
    df_county = df[['County','Onset Date','Case Count','Death Count','Hospitalized Count']]
    df_county['Case Count'] = df_county['Case Count'].str.replace(',','').astype(int)
    #df_county['Death Count'] = df_county['Death Count']#.str.replace(',','').astype(int)
    #df_county['Hospitalized Count'] = df_county['Hospitalized Count']#.str.replace(',','').astype(int)
    df_county = df_county.set_index(['County','Onset Date']).groupby(['County','Onset Date']).sum()
    d = df_county.loc[county].to_dict()
    return jsonify(d)

@app.route('/death/')
def death_count():
    oh_url = r'https://coronavirus.ohio.gov/static/COVIDSummaryData.csv'
    df = pd.read_csv(oh_url)
    df_county = df[['Date Of Death','Case Count','Death Count','Hospitalized Count']]
    df_county['Case Count'] = df_county['Case Count'].str.replace(',','').astype(int)
    #df_county['Death Count'] = df_county['Death Count']#.str.replace(',','').astype(int)
    #df_county['Hospitalized Count'] = df_county['Hospitalized Count']#.str.replace(',','').astype(int)
    df_county = df_county.set_index(['Date Of Death']).groupby(['Date Of Death']).sum()
    d = df_county.to_dict()
    return jsonify(d)

@app.route('/age/')
def age_group():
    oh_url = r'https://coronavirus.ohio.gov/static/COVIDSummaryData.csv'
    df = pd.read_csv(oh_url)
    df_county = df[['Age Range','Case Count','Death Count','Hospitalized Count']]
    df_county['Case Count'] = df_county['Case Count'].str.replace(',','').astype(int)
    #df_county['Death Count'] = df_county['Death Count'].str.replace(',','')#.astype(int)
    #df_county['Hospitalized Count'] = df_county['Hospitalized Count']#.str.replace(',','').astype(int)
    df_county = df_county.set_index(['Age Range']).groupby(['Age Range']).sum()
    d = df_county.to_dict()
    return jsonify(d)
if __name__ =='__main__':
    app.run()
from flask import jsonify, Flask, render_template
import pandas as pd
from flask_heroku import Heroku


app = Flask(__name__)
heroku = Heroku(app)

oh_url = r'https://coronavirus.ohio.gov/static/COVIDSummaryData.csv'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/all/') # This pulls all the data from the ODH
def all_data():
    oh_url = r'https://coronavirus.ohio.gov/static/COVIDSummaryData.csv'
    df = pd.read_csv(oh_url)
    print(df.head(10))
    d  = df.to_dict()
    return jsonify(d)

@app.route('/county/')
def county_data():
    oh_url = r'https://coronavirus.ohio.gov/static/COVIDSummaryData.csv'
    df = pd.read_csv(oh_url).groupby(['County']).sum()
    d = df.to_dict()
    return jsonify(d)
    
@app.route('/county/<county>/')
def county_lookup(county):
    oh_url = r'https://coronavirus.ohio.gov/static/COVIDSummaryData.csv'
    df = pd.read_csv(oh_url).set_index(['County']).groupby(['County']).sum()
    d = df.loc[county].to_dict()
    return jsonify(d)

@app.route('/sex/')
def sex():
    oh_url = r'https://coronavirus.ohio.gov/static/COVIDSummaryData.csv'
    df = pd.read_csv(oh_url).set_index(['Sex']).groupby(['Sex']).sum()
    d = df.to_dict()
    return jsonify(d)

@app.route('/onset/date/')
def onset_date():
    oh_url = r'https://coronavirus.ohio.gov/static/COVIDSummaryData.csv'
    df = pd.read_csv(oh_url).set_index(['Onset Date']).groupby(['Onset Date']).sum()
    d = df.to_dict()
    return jsonify(d)

@app.route('/onset/date/<county>/')
def onset_date_county(county):
    oh_url = r'https://coronavirus.ohio.gov/static/COVIDSummaryData.csv'
    df = pd.read_csv(oh_url).set_index(['County']).groupby(['County','Onset Date']).sum().sort_values(['Onset Date'])
    d = df.loc[county].to_dict()
    return jsonify(d)

@app.route('/death/')
def death_count():
    oh_url = r'https://coronavirus.ohio.gov/static/COVIDSummaryData.csv'
    df = pd.read_csv(oh_url).set_index(['Date Of Death']).groupby(['Date Of Death']).sum()
    d = df.to_dict()
    return jsonify(d)

@app.route('/age/')
def age_group():
    oh_url = r'https://coronavirus.ohio.gov/static/COVIDSummaryData.csv'
    df = pd.read_csv(oh_url).set_index(['Age Range']).groupby(['Age Range']).sum()
    d = df.to_dict()
    return jsonify(d)


if __name__ =='__main__':
    app.run()
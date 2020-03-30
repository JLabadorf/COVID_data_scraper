# Ohio COVID-19 Public Data
*SOURCE:Ohio Department of Health* 

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)


## PURPOSE
This API is designed to help data users get publically available information from the Ohio Department of Health. Other states are in the work. Anyone interested in helping develop this, please email james@jameslabadorf.com.
## API ROUTES
This is simply an API bridge for the data. All data is pulled when the API request is made. The Ohio Department of Health updates their data at 2:00PM EST. 
### `'/all/'`
returns all the data, unfiltered. 

### `'/county/'`
This route summarizes all data on the county level. This returns the data in two sets, one for Hospitalizations and another for deaths.

### `'/county/<county>/'`
This API route returns data based on the county queried. replace `<county>` with the county you wish to query.

### `'/sex/'` 
This API route returns data summerized on the sex of the patient.

### `'/onset/date/'`
This API route returns the data summerized by date of onset of symptons

### `'/onset/date/<county>'`
This API route returns the data summerized by date of onset filtered on the queried county. 
### `'/death/'`
This API route summarizes the data based on date of death. 

### `'/age/'`
This API route summarizes the data by age group.
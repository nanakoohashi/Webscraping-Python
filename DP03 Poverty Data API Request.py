# import packages
import requests as r
import addfips
import json
import pandas as pd

# establish FIPS codes
af = addfips.AddFIPS()
FIPS_cd = af.get_county_fips('Park', state='Wyoming')
state_code = FIPS_cd[:2]
county_list = ['Big Horn', 'Fremont', 'Hot Springs', 'Johnson', 'Park', 'Sheridan', 'Washakie']
FIPS_list = []
for i in range (len(county_list)):
    af = addfips.AddFIPS()
    FIPS_cd = af.get_county_fips(county_list[i], state='Wyoming')
    appender_fips = FIPS_cd[2:]
    FIPS_list.append(appender_fips)

# set column names
poverty_columns = ['Poverty Rate', 'Child Poverty Rate (<18)', 'Child Poverty Rate (<5)', 'Family Poverty', 
'Poverty Among Families with Children (<18)', 'Poverty Among Families with Children (<5)', 'Poverty Among Single-Female Families', 
'Poverty Among Single-Female Families with Children Under 18','State','County']

# establish DP03 poverty parameters
poverty_parameter = '?get=DP03_0128PE,DP03_0129PE,DP03_0131PE,DP03_0119PE,DP03_0120PE,DP03_0121PE,DP03_0125PE,DP03_0126PE'

# create empty list for the dataframes to append into
newdflist = []

# request API data and append dataframes into empty list (newdflist)
for i in range (len(FIPS_list)):
        request = r.get('https://api.census.gov/data/2018/acs/acs5/profile' + poverty_parameter + '&for=county:' + str(FIPS_list[i]) + '&in=state:' + str(state_code)) 
        eolas = request.json()
        df = pd.DataFrame.from_dict(eolas)
        newdflist.append(df[1:2]) 

# combine dataframes together 
dataset = pd.concat(newdflist)
dataset.columns = poverty_columns
dataset.index = county_list

# verify that the data is correct
print(dataset.head(10))
        
# export to csv
dataset.to_csv('ABSHSpovertydata.csv')
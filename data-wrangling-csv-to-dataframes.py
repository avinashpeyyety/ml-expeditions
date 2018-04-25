import csv
import pandas as pd
from pandas import DataFrame, Series
import numpy

#open csv from machine using pandas and directly creating a dataframe
reader1 = pd.read_csv('C:\omnica\data\olympics.csv')
print read,'\n'
    
#open and read csv file from local machine without pandas
with open('C:\omnica\data\olympics.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    list_of_dicts = []
    
    #create a list of dictionaries
    for line in reader:
        list_of_dicts.append(line)
    print list_of_dicts,'\n'
        
#Turn a list of dicts into a dict of lists.  Assumes all dicts in the list have the exact same keys."""    
def transposeDict(list_of_dicts):
    keys = list_of_dicts[0].iterkeys()
    return {key: [d[key] for d in list_of_dicts] for key in keys}
    
#create a dictionary of lists
dict_of_lists = transposeDict(list_of_dicts)
print dict_of_lists,'\n'
        
#convert the list of values for each key in dictionary to Series
countries = Series(dict_of_lists['countries'])
gold = Series(dict_of_lists['gold'])
silver = Series(dict_of_lists['silver'])
bronze= Series(dict_of_lists['bronze'])
       
#construct a dictionary of Series' that can be turned in to a DataFrame
medal_tally_dict = {'countries' : countries, 'gold': gold, 'silver': silver, 'bronze': bronze}
df = DataFrame(medal_tally_dict)
print df,'\n'

#DataFrame and Series properties
print df[['countries','gold']],'\n'
print df.describe(),'\n'
print 'The gold series in the dataframe is of dtype : ',df['gold'].dtype 
print 'Number countries : ',len(df['countries'])  
print 'The mean of golds won where bronze medals greater than 5 : ',df['gold'][df['bronze']>=2].mean()
print 'Mean of gold and bronze medal counts : ',(df['gold']+df['silver']).mean()
print 'Mean of golds : ',df['gold'].mean()
print 'Mean of bronzes : ',df['bronze'].mean()
print 'Max number of golds won by a country : ',df['gold'].max()
print 'Sum of golds won by all countries : ',df['gold'].sum()

# WIP
def standardize_data(values):
    standardized_values = (values - values.mean() ) / values.std()
    print standardized_values,'\n'

with open('C:\omnica\data\managers1.csv','w') as csvfile:
     fieldnames = ['first','second','third','fourth']
     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #writer.writeheader()
    #writer.writerow({'first' : 'avi', 'second' : 'aninda', 'third' : 'anuragSaketh', 'fourth' : 'RanaAditya'}) 

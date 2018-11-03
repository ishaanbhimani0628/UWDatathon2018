import pandas
import numpy
import sklearn
import matplotlib

kickstarter_data = pandas.read_csv('kickstarter201801.csv')
#print(kickstarter_data.head())
print(kickstarter_data.info())
print(kickstarter_data.describe())
kickstarter_data = kickstarter_data.drop(['ID','usd_pledged_real'], axis = 1)
print(kickstarter_data.head())
kickstarter_data.to_csv('kickstarter_dataset_edited.csv')
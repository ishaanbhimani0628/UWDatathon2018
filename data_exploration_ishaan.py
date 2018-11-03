import pandas
import numpy
import sklearn
import matplotlib.pyplot as plt


#Initial wrangling
# kickstarter_data = pandas.read_csv('kickstarter201801.csv')
# #print(kickstarter_data.head())
# print(kickstarter_data.info())
# print(kickstarter_data.describe())
# kickstarter_data = kickstarter_data.drop(['ID','usd_pledged_real'], axis = 1)
# print(kickstarter_data.head())
# kickstarter_data.to_csv('kickstarter_dataset_edited.csv')

#Working with the new dataset:
kickstart_data = pandas.read_csv('kickstarter_dataset_edited.csv')
#plt.scatter(kickstart_data['usd_goal_real'], kickstart_data['usd pledged']) #tells us that don't set goal above 2million
# pandas.scatter_matrix(kickstart_data) #only plots numerical, not as useful
#plt.show()
#kickstart_data['category'].value_counts().to_csv('category.csv')
#kickstart_data['main_category'].value_counts().to_csv('main_category.csv')
#Plot categories vs usd_pledged
#Goals vs usd_pledged
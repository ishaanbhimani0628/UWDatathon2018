import pandas
import numpy
import sklearn
import matplotlib.pyplot as plt
import math
import json


#Initial wrangling
# kickstarter_data = pandas.read_csv('kickstarter201801.csv')
# #print(kickstarter_data.head())
# print(kickstarter_data.info())
# print(kickstarter_data.describe())
# kickstarter_data = kickstarter_data.drop(['ID','usd_pledged_real'], axis = 1)
# print(kickstarter_data.head())
# kickstarter_data.to_csv('kickstarter_dataset_edited.csv')

#Working with the new dataset:
# kickstart_data = pandas.read_csv('kickstarter_dataset_edited.csv')
# #kickstart_data.info()
# null_array = []
# median_usd_pledge = kickstart_data['usd pledged'].median()
# kickstart_data['usd pledged'].fillna(median_usd_pledge, inplace = True)
# games_item = (kickstart_data[kickstart_data.values == 'Games'])
# design_item = (kickstart_data[kickstart_data.values == 'Technology'])
# technology_item = (kickstart_data[kickstart_data.values == 'Design'])
# relevant_cats = pandas.concat([games_item,design_item,technology_item])
# relevant_cats.to_csv('relevant_categories.csv')
# games_item.to_csv('games.csv')
# design_item.to_csv('design.csv')
# technology_item.to_csv('technology.csv')


# value_counts = kickstart_data['main_category'].value_counts()
# total_pledged_categories = {
#     'Film & Video': 0,
#     'Music': 0,
#     'Publishing': 0,
#     'Games': 0,
#     'Technology': 0,
#     'Design': 0,
#     'Art': 0,
#     'Food': 0,
#     'Fashion': 0,
#     'Theater': 0,
#     'Comics': 0,
#     'Photography': 0,
#     'Crafts': 0,
#     'Journalism': 0,
#     'Dance': 0,
# }
# for index, row in kickstart_data.iterrows():
#     main_category = row['main_category']
#     pledge = row['usd pledged']
#     #print(pledge)
#     total_pledged_categories[main_category] = total_pledged_categories[main_category] + pledge
#
# #print(total_pledged_categories)
# pledged_per_categories = {
#     'Film & Video': 0,
#     'Music': 0,
#     'Publishing': 0,
#     'Games': 0,
#     'Technology': 0,
#     'Design': 0,
#     'Art': 0,
#     'Food': 0,
#     'Fashion': 0,
#     'Theater': 0,
#     'Comics': 0,
#     'Photography': 0,
#     'Crafts': 0,
#     'Journalism': 0,
#     'Dance': 0,
# }
# projects_per_categories = {
#     'Film & Video': 63585,
#     'Music': 51918,
#     'Publishing': 39874,
#     'Games': 35231,
#     'Technology': 32569,
#     'Design': 30070,
#     'Art': 28153,
#     'Food': 24602,
#     'Fashion': 22816,
#     'Theater': 10913,
#     'Comics': 10819,
#     'Photography': 10779,
#     'Crafts': 8809,
#     'Journalism': 4755,
#     'Dance': 3768,
# }
# for key in pledged_per_categories:
#     pledged_per_categories[key] = total_pledged_categories[key]/projects_per_categories[key]
# print(pledged_per_categories)
# with open ('pledge_proj_cat.json', 'w') as fp:
#     json.dump(pledged_per_categories, fp, indent=4)
#
# #plt.scatter(kickstart_data['usd_goal_real'], kickstart_data['usd pledged']) #tells us that don't set goal above 2million
# # pandas.scatter_matrix(kickstart_data) #only plots numerical, not as useful
# #plt.show()
# #kickstart_data['category'].value_counts().to_csv('category.csv')
# #kickstart_data['main_category'].value_counts().to_csv('main_category.csv')
# #Plot categories vs usd_pledged
# #Goals vs usd_pledged

games_data = pandas.read_csv('games.csv')
design_data = pandas.read_csv('design.csv')
tech_data = pandas.read_csv('technology.csv')

data_array = [games_data, design_data, tech_data]
data_keys = []
data_value_counts = []
for item in data_array:
    value_counts = item['category'].value_counts()
    data_value_counts.append(value_counts)
    print(data_value_counts)
    print(" ")
    keys = value_counts.keys()
    data_keys.append(keys)

print(data_keys)

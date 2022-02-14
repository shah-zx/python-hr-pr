import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Path of the file to read
iowa_file_path = 'F:\\Python Programs\\MachineLearning\\train.csv'

home_data = pd.read_csv(iowa_file_path)

# print(home_data)   

home_data.columns  # This will give me the home data's columns info

y = home_data.SalePrice

print(y)   # This will give me the prices

feature_names = ["LotArea" , 
"YearBuilt" , 
"1stFlrSF" , 
"2ndFlrSF" , 
"FullBath" , 
"BedroomAbvGr" , 
"TotRmsAbvGrd" ]

X = home_data[feature_names]
# print(X)

# Reviewing the data :

print(X.head())






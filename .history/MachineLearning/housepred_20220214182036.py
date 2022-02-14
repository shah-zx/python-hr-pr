import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Path of the file to read
houses_file_path = 'F:\\Python Programs\\MachineLearning\\train.csv'

home_data = pd.read_csv(houses_file_path)

# print(home_data)   

home_data.columns  # This will give me the home data's columns info

y = home_data.SalePrice

# print(y)   # This will give me the prices

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

# print(X.head())

houses_model = DecisionTreeRegressor(random_state = 1)

# Fitting  the model

houses_model.fit(X,y)


# Making the predictions : 

predictions = houses_model.predict(X.head())
print("Your top few predictions of prices for the houses are as follows: ")
print("All the prices are in $")

for i in predictions:
    print(i , end="$")
    
    
    
    
    











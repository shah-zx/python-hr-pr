import pandas as pd
import numpy as np
import seaborn as sns

dataset = pd.read_excel("F:\\Python Programs\\Quantium data analytics\\QVI_transaction_data.xlsx")
# print(dataset.head())


# SUMMARIZATION

# print(dataset.describe())

# print(dataset.isnull().sum())

# sns.displot(dataset.TOT_SALES , kde= True)

numericdata = dataset.select_dtypes(['float' , 'int'])
# print(numericdata.head())


# REMOVING OUTLAYERS

x = numericdata[numericdata['TOT_SALES'] < 8.000]

print(sns.displot(x.TOT_SALES , kde = True))


# CHECKING FOR OUTLAYERS

print(sns.boxplot(x.TOT_SALES))


# DATA FORMAT 

print(dataset.dtypes)

# All of these is our first task 






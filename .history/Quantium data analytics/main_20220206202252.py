import pandas as pd
import numpy as np
import seaborn as sns

dataset = pd.read_excel("F:\\Python Programs\\Quantium data analytics\\QVI_transaction_data.xlsx")
# print(dataset.head())

# print(dataset.describe())

# print(dataset.isnull().sum())

# sns.displot(dataset.TOT_SALES , kde= True)

numericdata = dataset.select_dtypes(['float' , 'int'])
print(numericdata.head())

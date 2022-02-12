import pandas as pd
import numpy as np
import seaborn as sns

dataset = pd.read_csv("F:\\Python Programs\\Quantium data analytics\\Task-2\\QVI_data.csv")
print(dataset.head())
total_sales = sum(dataset['TOT_SALES'])
print(total_sales)


# There is not any customer column in dataset but we can get customers by text id because it is unique for every individual 

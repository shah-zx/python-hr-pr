import pandas as pd
import numpy as np

dataset = pd.read_csv("F:\\Python Programs\\Quantium data analytics\\Task-2\\QVI_data.csv")
print(dataset.head())

# TOTAL SALES REVENUE

total_sales = sum(dataset['TOT_SALES'])
print(total_sales)


# There is not any customer column in dataset but we can get customers by TX_ID because it is unique for every individual 

print(dataset.describe())

# TOTAL CUSTOMER

Total_customer = 241584

# TOTAL NUMBER OF TRANSACTION PER CUSTOMER

print(dataset.shape)

avg_trns = Total_customer / 264834

print(avg_trns)
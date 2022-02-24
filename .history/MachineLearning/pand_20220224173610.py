from operator import index
import pandas as pd
import numpy as np
# Making a dataframe :
Df = pd.DataFrame(np.arange(0, 20).reshape(5, 4), index=[
                  'Row1', 'Row2', 'Row3', 'Row4', 'Row5'], columns=['Column1', 'Column2', 'Column3', 'Column4'])

# print(Df)


sf = pd.DataFrame(np.arange(0, 40).reshape(4, 10),
                  index=['Row1', 'Row2', 'Row3', 'Row4'] , columns = ['Column1', 'Column2', 'Column3' , 'Column4'  , 'Column5'  , 'Column6' ,'Column7' ,'Column8' , 'Column9' ,'Column10'])
# print(sf)

# We can also change this data into an excel sheet :

sf.to_csv('forty.csv')

# print(Df.loc['Row3'])

# print(Df.iloc[0:2,0:2])

# this will give us the rows and columns 

# print(Df.iloc[0:3])

# print(type(Df.iloc[0:2,0:2]))

print(type(Df.iloc[0:2 ,0]))

















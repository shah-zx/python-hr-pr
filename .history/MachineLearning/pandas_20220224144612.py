from operator import index
import pandas as pd
import numpy as np
# Making a dataframe :
Df = pd.DataFrame(np.arange(0, 20).reshape(5, 4), index=[
                  'Row1', 'Row2', 'Row3'], columns=['col1', 'col2', 'col3'])
print(Df)

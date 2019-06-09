# In Data munging, you can convert a particular data into a different format. For example, if you have a .csv file, you can convert it into .html or any other data format as well. So, let me implement this practically.

import pandas as pd
 
country= pd.read_csv("/home/gautam/ai-training/Module 2/Pandas_Example/world-bank-youth-unemployment.csv",index_col=0)
 
country.to_html('edu.html')
# Next in python pandas tutorial, we’ll understand how to change the index values in a dataframe. For example, let us create a dataframe with some key value pairs in a dictionary and change the index values. Consider the example below: 


import pandas as pd
 
df= pd.DataFrame({"Day":[1,2,3,4], "Visitors":[200, 100,230,300], "Bounce_Rate":[20,45,60,10]}) 
 
df.set_index("Day", inplace= True)
 
print(df)
# Let us now change the headers of column in this python pandas tutorial. Let us take the same example, where I will change the column header from “Visitors” to “Users”. So, let me implement it practically.


import pandas as pd
 
df = pd.DataFrame({"Day":[1,2,3,4], "Visitors":[200, 100,230,300], "Bounce_Rate":[20,45,60,10]})
 
df = df.rename(columns={"Visitors":"Users"})
 
print(df)
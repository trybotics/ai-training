import pandas as pd

# 1....................................................................................................................

# Simple merging

df1= pd.DataFrame({ "HPI":[80,90,70,60],"Int_Rate":[2,1,2,3],"IND_GDP":[50,45,45,67]}, index=[2001, 2002,2003,2004])
 
df2=pd.DataFrame({ "HPI":[80,90,70,60],"Int_Rate":[2,1,2,3],"IND_GDP":[50,45,45,67]}, index=[2005, 2006,2007,2008])
 
merged= pd.merge(df1,df2)

print("First Data Frame",df1)
print("Second Data Frame",df2)
 
print(merged)

# 2....................................................................................................................

# Now, you can also specify the column which you want to make common.

# df1 = pd.DataFrame({"HPI":[80,90,70,60],"Int_Rate":[2,1,2,3], "IND_GDP":[50,45,45,67]}, index=[2001, 2002,2003,2004])
 
# df2 = pd.DataFrame({"HPI":[80,90,70,60],"Int_Rate":[2,1,2,3],"IND_GDP":[50,45,45,67]}, index=[2005, 2006,2007,2008])
 
# merged= pd.merge(df1,df2,on ="HPI")
 
# print(merged)

# 3....................................................................................................................

# joining 

# df1 = pd.DataFrame({"Int_Rate":[2,1,2,3], "IND_GDP":[50,45,45,67]}, index=[2001, 2002,2003,2004])
 
# df2 = pd.DataFrame({"Low_Tier_HPI":[50,45,67,34],"Unemployment":[1,3,5,6]}, index=[2001, 2003,2004,2004])
 
# joined= df1.join(df2)
# print(joined)
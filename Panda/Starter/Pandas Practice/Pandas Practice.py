import pandas as pd

#Reading CSV
df = pd.read_csv("customers.csv")

#Series
Customers = {"Mike":20, "Jack":30}

var = pd.Series(Customers, index=["Mike"])



#Output
print(var)
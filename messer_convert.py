import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df =pd.read_csv("C:/messer/data/messer_data_20191121.csv",sep=";",decimal=",",date_parser=".")
df2=pd.read_csv("C:/messer/data/messer_data_20191122.csv",sep=";",decimal=",",date_parser=".")
df3=pd.read_csv("C:/messer/data/messer_data_20191123.csv",sep=";",decimal=",",date_parser=".")
df4=pd.read_csv("C:/messer/data/messer_data_20191124.csv",sep=";",decimal=",",date_parser=".")


df=df.append(df2,ignore_index=True)
df=df.append(df3,ignore_index=True)
df=df.append(df4,ignore_index=True)


print(df)
print(df2)
print(df3)

print("hello")
a=list(df["PSA mennyiség: [m3]"])
ind=list(df["Dátum Idõ"])
print(a)
plt.plot(ind,df["PSA mennyiség: [m3]"])
plt.show();
print("ADFULLER")
from statsmodels.tsa.stattools import adfuller
result = adfuller(df2["PSA mennyiség: [m3]"].values)

print('p-value: %f' % result[1])

print("0.05 alatt kellene lennie")



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
files=os.listdir("C:/messer/data/")
print(files)
df=pd.read_csv("C:/messer/data/messer_data_20191121.csv",sep=";",decimal=",",date_parser=".")
for i in files[1:]:
    print(i)
    df2=pd.read_csv("C:/messer/data/"+i,sep=";",decimal=",",date_parser=".")
    df=df.append(df2,ignore_index=True)



print(df)


print("hello")
a=list(df["PSA mennyiség: [m3]"])
ind=list(df["Dátum Idõ"])
#print(a)
#plt.plot(ind,df["PSA mennyiség: [m3]"])
#plt.show();
df["Dátum Idõ"]=pd.to_datetime(df["Dátum Idõ"],format="%Y.%m.%d %H:%M:%S")
df.index
print(df.dtypes)
print("ADFULLER")
from statsmodels.tsa.stattools import adfuller
result = adfuller(df2["PSA mennyiség: [m3]"].values)

print('p-value: %f' % result[1])

print("0.05 alatt kellene lennie")

#print(df.corr(method="spearman"))
print(df.head())
print(df.columns)
df.columns=["timeStamp","LIN_V","LIN_P","PSA_M","PSA_P","PSA_Q","NONE"]
print(df.head())
df.drop(["NONE"],axis=1,inplace=True)
print(df.head())
df.to_csv("C:/messer/data/all.csv")

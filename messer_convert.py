import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("C:/messer/data/messer_data_20191122.csv",sep=";",decimal=",",date_parser=".")
print(df)
print("hello")
a=list(df["PSA mennyiség: [m3]"])
ind=list(df["Dátum Idõ"])
print(a)
#plt.plot(ind,df["PSA mennyiség: [m3]"])
#plt.show()
print("ADFULLER")
from statsmodels.tsa.stattools import adfuller
result = adfuller(df[3].values)

print('p-value: %f' % result[1])

print("0.05 alatt kellene lennie")
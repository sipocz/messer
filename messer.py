import requests
import pandas as pd
import time
import datetime

from bs4 import BeautifulSoup

def i2str(i):
    i2=str(i)
    if len(i2)<2:
        i2="0"+i2
    return(i2)


def readconfig():
    f=open("./messer.ini")
    config = {}

    for fs in f:
        fs=fs.strip()
        print(fs)
        confline = fs.split("=")
        config[confline[0]] = confline[1]

    f.close()
    print(config)
    return(config)

confline=readconfig()


if "path" in confline:
    path=confline["path"]
if "prefix" in confline:
    prefix=confline["prefix"]


print(path+prefix)





def getdata(t1,t2):
    print(t1)
    print(t2)
    y1=i2str(t1.year)
    m1=i2str(t1.month)
    d1=i2str(t1.day)


    y2=i2str(t2.year)
    m2=i2str(t2.month)
    d2=i2str(t2.day)


    print(y1,m1,d1)
    print(y2,m2,d2)



    print(dt)


    url1="http://telemetry.messer.hu:8080/cgi-bin/rview.exe?Log=..%5C..%5C..%5Cppsrv%5CRichter1.txt&Html=Richter1log&MaxRows="
    url2="10000&Year1="+y2+"&Mon1="+m2+"&Day1="+d2+"&Hour1=0&Year2="+y1+"&Mon2="+m1+"&Day2="+d1+"&Hour2=0"


    url=url1+url2


    fname=path+prefix+y2+m2+d2+".csv"


    print(url)
    result=requests.get(url)
    print(result.content)
    soup = BeautifulSoup(result.content, 'html.parser')
    print("----------------")
    #print(soup.prettify)
    #print(list(soup.children))
    allrow=soup.find_all("tr")[:]
    fo  = open(fname, "w",encoding='utf-8')
    for  row in allrow:
        #print(row)
        soup2=BeautifulSoup(result.content, 'html.parser')
        allcell=row.find_all("td")[:]
        sumcell=""
        #print("--------------")
        #print(allcell)
        for cell in allcell:
            celltxt=cell.text
            sumcell=sumcell+celltxt+";"

        outstr=sumcell.replace(".",",").replace(";"," ",1).replace(",",".",2).replace("   ","").replace("  ","")
        print(outstr)

        fo.write(outstr+"\n")

    # Close opend file
    fo.close()

dt=datetime.date.today()
t1=dt
dt=datetime.timedelta(days=110)
t1=t1-dt
for i in range(365):
    dt=datetime.timedelta(days=1)
    t2=t1-dt
    getdata(t1,t2)
    t1=t2
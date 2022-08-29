
import numpy as np
import pandas as pd

file =pd.read_csv('test_data.csv')
file_manager = file[file["role"]=='manager']
data_low=file_manager.text.str.lower()

a = data_low[data_low.str.contains((r'здра(?!$)|добрый день(?!$)|доброе утро(?!$)'))==True]
print(a)

b = data_low[data_low.str.contains((r'зовут(?!$)'))==True]
print(b)

c = b.to_string()
c = c.split()
ind=0
name = []
for i in c:
    if i == 'зовут':
        if c[ind-1]!='меня':
            name.append(c[ind-1])
        elif c[ind+1]!='меня':
            name.append(c[ind+1])
    ind+=1
print(name)

ind=0
company = []
for i in c:
    if i == 'компания':
        company.append(c[ind+1])
    ind+=1
print(company)

e = data_low[data_low.str.contains((r'до свид(?!$)|до встр(?!$)|доброго(?!$)'))==True]
print(e)

if len(a)!=len(e):
    if len(a)>len(e):
        for i in range(len(e)):
            if not(a.index[i]<b.index[i] and b.index[i]<e.index[i]):
                print("The manager is not greeted in {} dialogue".format(i))
        for i in range(len(e), len(a)):
            print("The manager is not greeted in {} dialogue".format(i))
    else:
        for i in range(len(a)):
            if not(a.index[i]<b.index[i] and b.index[i]<e.index[i]):
                print("The manager is not greeted in {} dialogue".format(i))
        for i in range(len(a), len(e)):
            print("The manager is not greeted in {} dialogue".format(i)) 
         






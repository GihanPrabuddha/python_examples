# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 18:42:25 2020

@author: GIhan
"""
import pandas as pd
import re

# Empty list to hold selected sheets
keyList = []

# Load excel file with all the sheets
df = pd.read_excel('Book1PY.xlsx', sheet_name=None)

# get list of relevet sheets
for aKey in df.keys():
  x = re.search("^SheetA.*", aKey)
  if (x):
    keyList.append(aKey)

df2 = { your_key: df[your_key] for your_key in keyList}

df3 = pd.concat(df2, ignore_index=True)




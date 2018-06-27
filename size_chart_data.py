# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 20:04:14 2018

@author: Om
"""

import pandas as pd
df_in = pd.read_excel("input.xlsx")
df_out = pd.DataFrame(columns = ["BRAND","FABRIC TYPE","BRICK","SIZE",
                                 "ALT BRAND","ALT SIZE"])

for index,row in df_in.iterrows():
    _BRAND=row["BRAND"]
    _FABRICTYPE=row["FABRIC TYPE"]
    _BRICK=row["BRICK"]
    _SIZE=row["SIZE"]
    _BUST=row["BUST"]
    pd_temp = df_in.loc[
            df_in['FABRIC TYPE'] == _FABRICTYPE].loc[
                    df_in['BRICK'] == _BRICK].loc[
                            abs(df_in["BUST"] - _BUST) <= 1]
    for index2, row2 in pd_temp.iterrows():
        df_append = pd.DataFrame(columns = ["BRAND","FABRIC TYPE","BRICK","SIZE",
                                 "ALT BRAND","ALT SIZE"],index=range(1))
        df_append.iloc[0]["BRAND"] = _BRAND
        df_append.iloc[0]["FABRIC TYPE"] = _FABRICTYPE
        df_append.iloc[0]["BRICK"] = _BRICK
        df_append.iloc[0]["SIZE"] = _SIZE
        df_append.iloc[0]["ALT BRAND"] = row2["BRAND"]
        df_append.iloc[0]["ALT SIZE"] = row2["SIZE"]
#        if True:                    # Uncomment to include own brand in output
        if _BRAND != row2["BRAND"]: # Uncomment to exclude own brand in output
            df_out = df_out.append(df_append,ignore_index = True)

df_out.to_excel("output.xlsx")
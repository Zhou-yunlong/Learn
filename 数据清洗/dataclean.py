# -*- coding: UTF-8 -*-
# created by Long on 2022/7/21 23:39
# @Software : PyCharm
import pandas as pd
import numpy as np
df = pd.read_csv("movie.csv", index_col=0)
# print(df.head())
print(df.info())
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 14:48:36 2019

@author: Cyril
"""

# Load the Pandas libraries with alias 'pd' 
import pandas as pd 
import numpy as np
#import os

# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
nameList = ["RefList", "reader", "date", "time", "TimeStamp", "Tagid", "ReaderAnt", "Freq", "Rssi", "phase"]
nbTagsParList = 25

data_21dbm = pd.read_csv("Inventory 2019-01-22 10-07-45 21dBm.csv", sep=';', names=nameList, index_col=False)
data_24dbm = pd.read_csv("Inventory 2019-01-22 09-56-51 24dBm.csv", sep=';', names=nameList, index_col=False)
data_27dbm = pd.read_csv("Inventory 2019-01-22 10-02-50 27dBm.csv", sep=';', names=nameList, index_col=False)
data_30dbm = pd.read_csv("Inventory 2019-01-22 09-10-13 30dBm.csv", sep=';', names=nameList, index_col=False)


#to show first 5 rows
#data_30dbm.head()

nbTagsLusParReflist = data_24dbm.groupby('RefList').Tagid.nunique()

#read rate = nb tag lus / nb tags total de tags qui passent par les portes
readRate = (nbTagsLusParReflist[0] + nbTagsLusParReflist[1]) / (2 * nbTagsParList)




tagList = data_30dbm.Tagid.unique()


#door detection program
doorA = [3,4]
doorB = [1,2]







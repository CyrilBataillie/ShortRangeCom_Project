# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 14:48:36 2019

@author: Cyril
"""

# Load the Pandas libraries with alias 'pd' 
import pandas as pd 
import numpy as np


nameList = ["RefList", "reader", "date", "time", "TimeStamp", "Tagid", "ReaderAnt", "Freq", "Rssi", "phase"]
nbTagsParList = 25

data_21dbm = pd.read_csv("Inventory 2019-01-22 10-07-45 21dBm.csv", sep=';', names=nameList, index_col=False)
data_24dbm = pd.read_csv("Inventory 2019-01-22 09-56-51 24dBm.csv", sep=';', names=nameList, index_col=False)
data_27dbm = pd.read_csv("Inventory 2019-01-22 10-02-50 27dBm.csv", sep=';', names=nameList, index_col=False)
data_30dbm = pd.read_csv("Inventory 2019-01-22 09-10-13 30dBm.csv", sep=';', names=nameList, index_col=False)

data = data_30dbm


tagList = data_30dbm.Tagid.unique()
readTagList = data.Tagid.unique()
nbTagsLusParReflist = data.groupby('RefList').Tagid.nunique()



doorA = [1,2] #doorA with reader 1 and 2
doorB = [3,4] #doorA with reader 3 and 4
nbGoodDoors = 0
nbGoodDoors2 = 0

tagsInDoorA = []
tagsInDoorB = []
badAssociation = []

for tag in readTagList:
    m = data['Tagid'] == tag
    extractWithReadTag = data.where(m)
    listReadersForThisTag = extractWithReadTag.ReaderAnt.unique()
    listRefListForThisTag = extractWithReadTag.RefList.unique()
    
    goodDoor = False
    interA = np.intersect1d(listReadersForThisTag, doorA)
    interB = np.intersect1d(listReadersForThisTag, doorB)
    
    if (len(interA)>0 and not len(interB)>0) or (len(interB)>0 and not len(interA)>0):
        goodDoor = True
        nbGoodDoors += 1

    else:
        extractDoorA1 = extractWithReadTag[extractWithReadTag['ReaderAnt'] == 1]
        extractDoorA2 = extractWithReadTag[extractWithReadTag['ReaderAnt'] == 2]
        extractDoorA = pd.concat([extractDoorA1, extractDoorA2])
        
        extractDoorB3 = extractWithReadTag[extractWithReadTag['ReaderAnt'] == 3]
        extractDoorB4 = extractWithReadTag[extractWithReadTag['ReaderAnt'] == 4]
        extractDoorB = pd.concat([extractDoorB3, extractDoorB4])
        
        avgRssiA = extractDoorA.Rssi.mean()
        avgRssiB = extractDoorB.Rssi.mean()
        
        if (avgRssiA > avgRssiB):
            tagsInDoorA.append(tag)
            
            if "Reference List 3" in listRefListForThisTag:
                goodDoor = True
            else:
                tagsInDoorA.pop()
                badAssociation.append(tag)
            
        elif (avgRssiB > avgRssiA):
            tagsInDoorB.append(tag)
            
            if "Reference List 4" in listRefListForThisTag:
                goodDoor = True
            else:
                tagsInDoorB.pop()
                badAssociation.append(tag)
        
        else:
            badAssociation.append(tag)

    if (goodDoor):
        nbGoodDoors2 += 1

   
#read rate = nb tag lus / nb tags total de tags qui passent par les portes
readRate = (len(readTagList)) / (2 * nbTagsParList)

    
#assocation rate = nb tag lus uniquement par la bonne porte / nb total de tags lus          
associationRate = nbGoodDoors / len(readTagList)
associationRateAfterImprovement = nbGoodDoors2 / len(readTagList)
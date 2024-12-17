#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 00:15:38 2024

@author: samanthalasse_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    # animal collection in MongoDB
    
    def __init__(self):
        # intialize MongoClient with user information
        USER = 'aacuser1'
        PASS = 'SNHU4321'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32460
        DB = 'ACC'
        COL = 'animals'
        
        #initalize connection
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
    # Method to implentment the C in CRUD
    def create(self, data):
        if data is not None:
            # new data, add to database
            self.database.animals.insert_one(data)
            # run a simple query to ensure inserting the data is successful
            
            if ObjectId is not None:
                return True
            else:
                return False
        else:
            raise Exception("No data to save")
            
    # Method to implement the R in CRUD
    
    def read(self, query):
        # read from database
        if query is not None:
            self.database.animals.find(query)
            return 
        else:
            self.database.animals.find()
            return
        
    def update(self, aID, replace):
        # made to update an item in a certain category for a certain animal (animal ID)
        if aID is not None and replace is not None:
            self.database.animals.update_one(aID, replace)
            # verify replacement
            update = self.database.animals.find(aID, replace)
            if update is not None:
                return 1
            else:
                return 0
        else:
            return
            
    def delete(self, aID):
        # delete an animal out of the database
        if aID is not None:
            self.database.animals.delete_one(aID)
            # check to see if deleted
            check = self.database.animals.find(aID)
            if check is None:
                return 1
            else:
                return None
        else:
            return
        
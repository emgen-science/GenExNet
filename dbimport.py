##############################################################
# Chuck Greenman, GNU GPL 2017                               #
# Despite the existence of the MongoImport command, this     #
# is a class about programming in python. So I've built      #
# a little importer utility.                                 #
#                                                            #
# WARNING: Mongo MUST be running as a service.               #
##############################################################

import sys
import csv
import pymongo
from pymongo import MongoClient

client = MongoClient()

def create_database(name):
    db = client[name]
    return db

def create_collection(database_object, collection_name):
    collection = database_object[collection_name]
    return collection

def ask_type(column_name):
    print("Tell us what kind of data this is:")
    print(column_name)
    print("(i)d\t(a)ttribute\t(d)on't use for classification")

"""def build_documents():
    with open() as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:"""

def main():
    print("##### IMPORT TOOL #####")

    database_name = input("Name Database: ")
    collection_name = input("Name Collection: ")
    file_name = input("Where is the CSV: ")

    database = create_database(database_name)
    collection = create_collection(database, collection_name)

    # build_documents(database, collection, file_name)

main()

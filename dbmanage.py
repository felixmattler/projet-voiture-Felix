# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 11:43:19 2021

@author: raffelet
"""
import sqlite3
import initdatabase as initdB
from pathlib import Path


def connect():
    my_file = Path(initdB.DATABASE)

    if my_file.is_file():
        conn = initdB.init()
    else:
        conn = initdB.dbCreate()
    return conn


def addDevice(model, autonomie,chargement, conn):
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO voitures(model, autonomie, chargement) VALUES(?,?,?)""", (model, autonomie, chargement))
    conn.commit()
    
def selectAll(conn):
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM voitures """)
    allDevice = cursor.fetchall()
    return allDevice


def selectModel(conn,name):
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM voitures WHERE model = '"""+name+"""'""")
    allDevice = cursor.fetchall()
    return allDevice


conn = connect()
# addDevice("tesla",'600',"30",conn)
# addDevice("Renault",'100',"30",conn)
initdB.end(conn)
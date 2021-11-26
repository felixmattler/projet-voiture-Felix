# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 15:20:44 2021

@author: raffelet
"""

import sqlite3
from pathlib import Path

DATABASE = './datab/prjsnmp.db'
        
def init():
    conn = sqlite3.connect(DATABASE)
    return conn

def returnPath(DATABASE):
    return DATABASE
    
def end(conn):
    conn.close()

def dbCreate():
    conn = init()
    initVoiture(conn)
    return conn

    
def initPoller(conn):
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS poller(
                           id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                           idDevices INTEGER,
                           idOids INTEGER,
                           timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                           timer INTEGER,
                           FOREIGN KEY (idDevices) REFERENCES devices(id),
                           FOREIGN KEY (idOids) REFERENCES oids(id)
                           )
                   """)
    conn.commit()

def initVoiture(conn):
    cursor = conn.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS voitures(
                           id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                           model TEXT,
                           autonomie TEXT,
                           chargement INTEGER
                           )
                   """)
    conn.commit()
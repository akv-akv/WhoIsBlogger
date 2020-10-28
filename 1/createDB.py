import sqlite3
import random as r
from datetime import date
from sqlite3 import Error

def create_connection(db_file):
    ''' create connection to sqlite database'''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        create_tables(conn)
        fill_users(conn)
        fill_items(conn)
        fill_purchases(conn)
        conn.commit()
        #print_table(conn,'Items')
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_tables(conn):
    """ Create tables for users, purchases and items"""
    c = conn.cursor()
    sql = """CREATE TABLE IF NOT EXISTS Users 
                    (userId INTEGER PRIMARY KEY ,
                     age INTEGER NOT NULL)"""
    c.execute(sql)
    sql = '''CREATE TABLE IF NOT EXISTS Purchases 
            (purchaseId INTEGER PRIMARY KEY, 
            userId INTEGER NOT NULL, 
            itemId INTEGER NOT NULL, 
            date TEXT)'''
    c.execute(sql)
    sql = '''CREATE TABLE IF NOT EXISTS Items
                (itemId INTEGER PRIMARY KEY,
                price INTEGER NOT NULL)'''
    c.execute(sql)

def fill_users(conn):
    """Fill users table with test data"""
    records = []
    for i in range(1,70,3):
        records.append((i,i+10))
        records.append((i+1,i+11))
        records.append((i+2,i+11))
    c = conn.cursor()
    c.executemany('INSERT INTO Users VALUES(?,?);',records)

def fill_items(conn):
    """Fill items table with test data"""
    records = []
    for i in range(1,10):
        records.append((i,i*50))
        c = conn.cursor()
    c.executemany('INSERT INTO Items VALUES(?,?);',records)

def fill_purchases(conn):
    """ Fill purchases table with test data"""
    records = []
    for i in range(1,10000):
        userId = r.randint(1,70)
        itemId = r.randint(1,10)
        year =  r.randint(2010,2020)
        month = r.randint(1,12)
        if month in [1,3,5,7,8,10,12]:
            day = r.randint(1,31)
        elif month == 2:
            day = r.randint(1,28)
        else:
            day = r.randint(1,30)
        random_day = date(year,month,day)
        records.append((i,userId,itemId,random_day))
    c = conn.cursor()
    c.executemany('INSERT INTO Purchases VALUES(?,?,?,?)',records)

def print_table(conn, table):
    """Print table contents for debugging purposes"""
    c = conn.cursor()
    c.execute('SELECT * FROM ' + table)
    rows = c.fetchall()
    for row in rows:
        print(row)

if __name__ == '__main__':
    create_connection('test.db')


import sqlite3 as db
import PySimpleGUI as sg
import time

class ProductsData():
    def __init__(self) -> None:
        try:
            self.connect = db.connect('database.db')
            cursor = self.connect.cursor()
        except db.Error as error:
            sg.popup(error)
        finally:    
            cursor.execute('''CREATE TABLE IF NOT EXISTS products(
                           product_id       INTEGER PRIMARY KEY,
                           product_text     CHAR(50),
                           quantity_stored  INTEGER,
                           data_created     DATETIME DEFAULT TIMESTAMP)
                           ''')
            cursor.close()

    def insertdata(self,product_id,product_text,quantity):
        try:
            cursor = self.connect.cursor()
        except db.Error as error:
            sg.popup(error)
        finally:
            cursor.execute(f'INSERT INTO products VALUES (?,?,?,?)'(product_id,product_text,quantity,time.time()))
            self.connect.commit()
            sg.popup('Data Saved')

    def selectdata(self):
        pass


class SupplierData():
    def __init__(self) -> None:
        try:
            self.connect = db.connect('database.db')
            cursor = self.connect.cursor()
        except db.error as error:
            sg.popup(error)
        finally:
            cursor.execute('''CREATE TABLE IF NOT EXISTS supplier(
                           supplier_id INT(10) PRIMARY KEY,
                           supplier_name CHAR(20),
                           supplier_email TEXT,
                           supplier_adress TEXT
            )
                          ''')
            cursor.close()
        

class CreateOrder():
    def __init__(self) -> None:
        try:
            self.connect = db.connect('database.db')
            cursor = self.connect.cursor()
        except db.Error as error:
            sg.popup(error)
        finally:
            cursor.execute('''CREATE TABLE IF NOT EXISTS orders(
                           order_header   INTEGER PRIMARY KEY,
                           order_item     INTEGER,
                           product_id     INTEGER,
                           quantity       INTEGER,
                           user           CHAR(10),
                           supplier_id    INT(10),
                           supplier_name  CHAR(20),
                           supplier_email TEXT
            )
                           ''')
            cursor.close()
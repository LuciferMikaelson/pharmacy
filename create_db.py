import sqlite3
def create_db():
    con=sqlite3.connect(database=r'pharmacy.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(100) NOT NULL, email VARCHAR(60) NOT NULL, gender TEXT NOT NULL, contact VARCHAR(20) NOT NULL, dob TEXT(10) NOT NULL, doj TEXT(10) NOT NULL, pass TEXT(80) NOT NULL, utype TEXT(50) NOT NULL, address TEXT NOT NULL, salary TEXT NOT NULL)")
    con.commit() 


    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(100) NOT NULL, contact TEXT NOT NULL, email VARCHAR(100) NOT NULL ,dese TEXT NOT NULL)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS category(c_id INTEGER PRIMARY KEY AUTOINCREMENT, c_name VARCHAR(100) NOT NULL)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,Category TEXT, Supplier TEXT, name VARCHAR(100) NOT NULL, price INTEGER, qty INTEGER, status TEXT NOT NULL)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS register(id INTEGER PRIMARY KEY AUTOINCREMENT,f_name VARCHAR(100) NOT NULL, l_name VARCHAR(100) NOT NULL, contact INTEGER NOT NULL, email VARCHAR(100) NOT NULL, question VARCHAR(100) NOT NULL, answer VARCHAR(100) NOT NULL, password VARCHAR(100) NOT NULL)")
    con.commit() 

    cur.execute("CREATE TABLE IF NOT EXISTS sales_history(bill_no INTEGER PRIMARY KEY ,c_name VARCHAR(100) NOT NULL, contact INTEGER NOT NULL, date VARCHAR(100) NOT NULL, product_name VARCHAR(100) NOT NULL, qty INTEGER NOT NULL, price VARCHAR(100) NOT NULL)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS purchase(invoice INTEGER PRIMARY KEY AUTOINCREMENT,Supplier TEXT NOT NULL ,pname TEXT(100) NOT NULL, quantity INTEGER NOT NULL, date VARCHAR(100) NOT NULL, type VARCHAR(100) NOT NULL, price INTEGER NOT NULL, status VARCHAR(100) NOT NULL)")
    con.commit()  

    # cur.execute("DROP TABLE supplier")
    # con.commit()

    # cur.execute("DROP TABLE product")
    # con.commit()

create_db()    
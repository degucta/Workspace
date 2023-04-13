# coding: utf-8

import xlwings as xw
import sqlite3
import logging as logger


# sample test method 
def copy_add_text():
    txt = xw.Range('A1').value
    txt += ', I am the Doctor.'
    xw.Range('B3').value = txt

#
# DESC: database connectivity check test 
# NOTE: How to return value(s) to caller explicitly needs to be worked out
#
def getDatabaseContent():

    logger.basicConfig(filename='std.log', filemode='a', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logger.INFO)
    logger.info('getDatabaseContent method invocation started')

    #txtQuery = xw.Range('A5').value
    conn = sqlite3.connect('C:/Workspace/testtest.db') # [2022/4/14]: "/" NOT "\"
    curs = conn.cursor()

    if doesTableExist(conn, curs, 'persons') == False: 
        # テーブル作成を指示する（コミットしないとDBに登録されないので要注意）
        print("Persons table does NOT exist - need to create")
        curs.execute(
            'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name String)'
        )
        conn.commit()
    else:
        print("Persons table already exists")
    
    # テーブルに値を挿入する
    curs.execute(
        'INSERT INTO persons(name) values("Taro")'
    )
    conn.commit()

    # 値を更新する
    curs.execute('UPDATE persons SET name = "Jiro" WHERE name = "Taro"')
    conn.commit()

    # 検索してコンソールに表示する
    curs.execute(
        'SELECT * FROM persons;'
    )

    #print(curs.fetchall())
    txtResult = curs.fetchall()

    # カーソルとDB接続を終了する
    curs.close()
    conn.close()

    # Dump the result back to caller worksheet - is this the only way ?
    #xw.Range('B16').value = txtResult
 
    return txtResult

## import mysql.connector
def mysqlDatabaseConnect():

## Now connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'

    conn = mysql.connector.connect(
    host='localhost',
    user='bookkeeper',
    password='Uzuki2022!',
    db='bookkeeper'
    )

    print(conn.is_connected())

    # カーソル作成
    cur = conn.cursor()
    cur.execute("select version()")
    print(cur.fetchone())

    #cur.execute("use bookkeeper; set @param1 = 0; call simpleproc(@param1); select @param1;")
    statement = 'call simpleproc(@param1); select @param1;';
    
    # call stored procedure via "callproc" method - Do NOT use "execute" method
    args = [0]
    result_args = cur.callproc('simpleproc', args)


    print("Stored procedure execution result is -->> ", result_args[0])

    #print(cur.fetchone())
    cur.close()


def doesTableExist(conn, cur, tableName):
    
    strStatement = """
        SELECT COUNT(*) FROM sqlite_master
        WHERE TYPE='table' AND name='""" + tableName + """'"""
    print("DEBUG"+ strStatement)

    cur.execute(strStatement)

    if cur.fetchone()[0] == 0:
        return False
    return True

def exceptionHandlingTest():
    try:
        a = int(input("Enter numerator number: "))
        b = int(input("Enter denominator number: "))
        print("Result of Division: " + str(a/b))
    # except block handling division by zero
    except(ZeroDivisionError):
        print("You have divided a number by zero, which is not allowed.")
    finally:
        print("Code execution Wrap up!")
    
    # outside the try-except block
    #print("Will this get printed?")
    print("ここはプリントされるかな")


def divisionCalc():
    a = int(input("Enter numerator number: "))
    b = int(input("Enter denominator number: "))
    import decimal

    decimal.getcontext().prec = 100
    division = decimal.Decimal(a) / decimal.Decimal(b)
    print(division)
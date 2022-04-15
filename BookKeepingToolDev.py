# coding: utf-8

import xlwings as xw
import sqlite3

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
    xw.Range('B16').value = txtResult
 
    return txtResult
    
def doesTableExist(conn, cur, tableName):
    
    strStatement = """
        SELECT COUNT(*) FROM sqlite_master
        WHERE TYPE='table' AND name='""" + tableName + """'"""
    print("DEBUG"+ strStatement)

    cur.execute(strStatement)

    if cur.fetchone()[0] == 0:
        return False
    return True

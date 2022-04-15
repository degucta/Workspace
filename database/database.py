import sqlite3

# インメモリーにしたい場合は':memory:'を引数に渡す
conn = sqlite3.connect('test.db')

# カーソル（こいつにどうして欲しいか指示をしていく）
curs = conn.cursor()

# テーブル作成を指示する（コミットしないとDBに登録されないので要注意）
curs.execute(
    'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name String)'
)
conn.commit()

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
print(curs.fetchall())

# カーソルとDB接続を終了する
curs.close()
conn.close()
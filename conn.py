import psycopg2

# 配置数据库连接参数
conn_params = {
    "dbname": "tiktokmsg",
    "user": "postgres",
    "password": "!QAZ2wsx",
    "host": "47.116.121.218",
    "port": "54320"
}


def sqlInsert(insertSql, datas):
    conn = psycopg2.connect(**conn_params)
    cur = conn.cursor()
    # 执行SQL语句
    cur.execute(insertSql, datas)
    # 提交事务
    conn.commit()
    # # 关闭游标和连接
    cur.close()
    conn.close()


def sqlUpdate(updateSql, datas):
    conn = psycopg2.connect(**conn_params)
    cur = conn.cursor()
    cur.execute(updateSql, datas)
    conn.commit()
    cur.close()
    conn.close()


def sqlSelect(selectSql):
    conn = psycopg2.connect(**conn_params)
    cur = conn.cursor()
    # 执行SQL语句
    cur.execute(selectSql)
    rows = cur.fetchall()
    # 提交事务
    conn.commit()
    return rows

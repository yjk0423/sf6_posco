# 도서 관리 데이터 베이스
# 동적 바인딩 방식 (? 기호 사용)
# db의 레코드(행)의 자료형은 튜플임
# 요소가 1개일때 (1,) , 을 사용해야함
import sqlite3


# table 생성

def getcon():
    conn = sqlite3.connect("./output/bookdb.db")
    return conn


def create_book():
    conn = getcon()
    cur = conn.cursor()
    sql = "create table book(book_no INTEGER PRIMARY KEY AUTOINCREMENT, title text not null, author text not null, price integer not null)"
    cur.execute(sql)
    conn.commit()
    conn.close()


def select_book():
    conn = getcon()
    cur = conn.cursor()
    sql = "select * from book;"
    cur.execute(sql)
    print(cur.fetchall())
    conn.close()


def select_one():
    conn = getcon()
    cur = conn.cursor()
    sql = "select * from book where book_no = ?"
    cur.execute(sql, (2,))
    print(cur.fetchone())
    conn.close()


def insert_book():
    conn = getcon()
    cur = conn.cursor()
    sql = "insert into book(title, author, price)values(?,?,?)"  # 동적 바인딩
    cur.execute(sql, ('점프 투 파이썬', '박응용', 19800))
    conn.commit()
    conn.close()


def update_book():
    conn = getcon()
    cur = conn.cursor()
    sql = "update book set price = ? where book_no = ?"
    cur.execute(sql, (15000, 1))
    conn.commit()
    conn.close()


def delete_book():
    conn = getcon()
    cur = conn.cursor()
    sql = "DELETE from book where book_no = ?"
    cur.execute(sql, (1,))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # create_book()
    # insert_book()
    # update_book()
    # delete_book()
    select_book()
    select_one()

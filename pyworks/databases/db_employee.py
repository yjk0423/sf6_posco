import sqlite3

# 사원 전체조회
def select_emp():
    conn = sqlite3.connect('c:/pydb/mydb.db') #db에 연결한다
    cur = conn.cursor() # 작업 객체 생성
    sql = "SELECT * FROM employee"
    cur.execute(sql)
    rs = cur.fetchall() # db에 있는 자료 모두 가져옴 자료구조는 리스트 이다. (rs - result_set) 리스트 요소는 튜플이다.
    print(rs)
    print(rs[0])
    conn.close()
def insert_emp():
    conn = sqlite3.connect('c:/pydb/mydb.db') #db에 연결한다
    cur = conn.cursor() # 작업 객체 생성
    sql = "INSERT INTO employee (emp_id, name, salary) VALUES('e105','조대리',4500000)"
    cur.execute(sql)
    conn.commit()   # 삽입후 커밋 해야함
    conn.close()
def update_emp():
    conn = sqlite3.connect('c:/pydb/mydb.db')  # db에 연결한다
    cur = conn.cursor()  # 작업 객체 생성
    sql = "UPDATE employee set salary = 2500000 where emp_id = 'e104'"
    cur.execute(sql)
    conn.commit()  # 삽입후 커밋 해야함
    conn.close()

def delete_emp():
    conn = sqlite3.connect('c:/pydb/mydb.db')  # db에 연결한다
    cur = conn.cursor()  # 작업 객체 생성
    sql = "Delete from employee where emp_id = 'e102'"
    cur.execute(sql)
    conn.commit()  # 삽입후 커밋 해야함
    conn.close()

def select_one():
    conn = sqlite3.connect('c:/pydb/mydb.db')  # db에 연결한다
    cur = conn.cursor()  # 작업 객체 생성
    sql = "select * from employee where name like '%신입%'"
    cur.execute(sql)
    rs = cur.fetchone() #db에서 반환 값
    print(rs)
    conn.close()
# insert_emp()
#update_emp()
select_emp()
select_one()
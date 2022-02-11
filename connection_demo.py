import pymysql as pymysql

server_name = "localhost"

user_name = "test"

password = "test"

dbname = "student"

connection = pymysql.connect(host=server_name,
                             user=user_name,
                             password=password,
                             db=dbname
                             )
with connection:
    # with connection.cursor() as cursor:
    #     # Create a new record
    #     sql = "INSERT INTO student_details (name,id,age,batch,is_passed_out,total_marks) VALUES ('hello',1,25,'2021-22',0,50);"
    #     cursor.execute(sql)
    #
    # # connection is not autocommit by default. So you must commit to save
    # # your changes.
    # connection.commit()

with connection.cursor() as cursor:
        # Read a single record
        sql = "select * from student_detail;"
        cursor.execute(sql)
        result = cursor.fetchall()
        # result = cursor.fetchone()
        print(result)
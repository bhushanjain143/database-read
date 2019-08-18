import pymysql
count=0
db = pymysql.connect(host='localhost', port=3306, user='abc', passwd='abc123', db='abc')
x="SN-MSS-05340\r"
cursor=db.cursor()
sql="select Total from student"
l=[]
try:
    z1=f"select * from top324 where service_id = '{x}' "
    cursor.execute(z1) 
    rs = cursor.fetchall()
    #print(rs)
    #iterate through rows
    for i in rs:
        k=list(i)
        #taking the first element from the list and append it to the list
        l.append(k[0])
    #db.commit() 
except:
    db.rollback()
db.close()
print(l)
if l != []:
    print("1")
else:
    print("0")
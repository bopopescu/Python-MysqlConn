#@author:Selçuk KADER
##14050111014
##Computer Engineering

#read name,age,gpa from the students.xml
import mysql.connector as conn
import xml.etree.ElementTree as ET
tree = ET.parse('C:\students.xml')
root = tree.getroot()

#read ıd(primary key) from the students.xml
from xml.dom import minidom
xmldoc = minidom.parse('C:\students.xml')
itemlist = xmldoc.getElementsByTagName('student')


#connect to server
db=conn.connect(host="127.0.0.1",user="testuser",password="test123")
cursor=db.cursor()
#create database
cursor.execute("""CREATE DATABASE IF NOT EXISTS TESTDB""")
db.commit()
#use database
cursor.execute("""USE TESTDB""")
db.commit()
#if exists drop 'STUDENTS' table
cursor.execute("""DROP TABLE IF EXISTS STUDENTS""")
db.commit()
#create table 'STUDENTS' with columns(ID,NAME,AGE,GPA)
cursor.execute("""CREATE TABLE IF NOT EXISTS STUDENTS(ID VARCHAR(20) PRIMARY KEY,NAME VARCHAR(100),AGE INT ,GPA FLOAT )""")
db.commit()

#for the read to buffer
cursor = db.cursor(buffered=True)

#declare a counter
j=0

#insert to 'STUDENTS' table with their values using a for loop
try:
         for j in range(0, 5):
            cursor.execute("""INSERT INTO STUDENTS(ID,NAME,AGE,GPA) VALUES (%s,%s,%s,%s)""",
                       (itemlist[j].attributes['id'].value,root[j][0].text, root[j][1].text, root[j][2].text))
            db.commit()

except:
         print()

cursor.execute("SELECT COUNT(*) ID FROM STUDENTS WHERE AGE>20")
f=cursor.fetchall()[0][0]
print('Number Of Students Whose Age Are Greater Than 20 == ',f,'Students')




#close the cursor object
cursor.close()



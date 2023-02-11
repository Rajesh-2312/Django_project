import email
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
import mysql.connector as sql
import pymysql 
from ast import Break
# Create your views here.

def signup(request):
    if request.method =="POST":
        email=request.POST['email']
        hno=request.POST['hno']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        con = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='#M21rk03s20l16',database='student_database',charset='utf8')
        with con:
            cur=con.cursor()
            cur.execute("select * FROM student_table")
            row = cur.fetchall()
            for Row in row:
                if Row[0]==email or Row[1]==hno:
                    print(Row[0],Row[1],Row[2])
                    status='success'
                    Break
                    messages.info(request,'Email or Halliticket Number is Already Taken!!!')
                    return render(request,'testapp/login.html')
        db_connection=pymysql.connect(host='127.0.0.1',port=3306, user='root',passwd='#M21rk03s20l16',database='student_database',charset='utf8')
        db_cursor = db_connection.cursor()
        student_sql_query = "INSERT INTO student_table(email_id,hallticket_no,passwd1,passwd2) VALUES ('"+email+"','"+hno+"','"+pass1+"','"+pass2+"')"
        if pass1==pass2:
            if len(hno)==10:
                db_cursor.execute(student_sql_query)
                db_connection.commit()
                messages.info(request,'account saved')
            print(db_cursor.rowcount,"Record inserted")
        if db_cursor.rowcount==1:
            
            
            messages.success(request,'Your Accout Created Successfully!!')
            return redirect('login')
        else:
            return redirect('signup')
     
    return render(request,'testapp/signup.html')
        
    


def login(request):
    if request.method == "POST":
        email=request.POST['email']
        hno=request.POST['hno']
        pass1=request.POST['password']
        status='none'
        con = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='#M21rk03s20l16',database='student_database',charset='utf8')
        with con:
            cur=con.cursor()
            cur.execute("select * FROM student_table")
            row = cur.fetchall()
            for Row in row:
                if Row[0]==email and Row[1]==hno and Row[2]==pass1:
                    print(Row[0],Row[1],Row[2])
                    status='success'
                    break
            if status == 'success':
                return render(request,'testapp/home.html')
            else:
                messages.info(request,'Bad Creditials')
                return render(request,'testapp/login.html')
    return render(request,'testapp/login.html')



def home(request):
    return render(request,'testapp/home.html')

def video(request):
    return render(request,'testapp/video.html')

def contents(request):
    return render(request,'testapp/contents.html')
def about(request):
    return render(request,'testapp/about.html')
def logout(request):
    return render(request,'testapp/login.html')
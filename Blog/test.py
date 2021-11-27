from flask import Flask, render_template, Response, request, redirect,flash
from pymysql import connect, cursors, Error
from datetime import datetime  
from docx import Document
from docx.shared import Inches
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'blog1',
    }
cnx = connect(**config)
# Chỉ định URL kích hoạt hàm homepage
@app.route('/index', methods = ["GET"])
def getpage():
    cur = cnx.cursor()
    sql="SELECT * FROM blog_user"
    cur.execute(sql)
    return render_template("index.html",cur=cur)

@app.route('/index', methods =["POST"])
def postpage():
    title = request.form["title"]
    content = request.form["content"]
    cur = cnx.cursor()
    sql="INSERT INTO blog_user (title, content, create_date) VALUES (%s, %s,%s)"
    value=(title,content,datetime.now())
    cur.execute(sql,value)
    cnx.commit()
    #cnx.close()
    return redirect("/index", code=302)



if __name__ == "__main__":
    # Chạy Flask app
    # Bật debug để restart server mỗi khi có thay đổi trong mã
    app.run(debug=True)

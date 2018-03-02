from flask import Flask,render_template,redirect,request
from sqlalchemy import create_engine,exc

app = Flask(__name__)

engine = create_engine('mysql://root@localhost:3306/fathomless')

connection = engine.connect()



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/insert',methods=['POST'])
def insert():

    #sanitize data

    name = request.form['name']
    email = request.form['email']
    sub = request.form['sub']
    dis = request.form['dis']
    b=False
    for x in name.split():
        if x.isalpha():
            b=True
        else:
            b=False
            break
    if name == "" or b==False or email == "" or sub == "" or dis == "":
        return render_template("index.html",failed=True)

    statement = "insert into user96 (name,email,sub,descr) values ('"+name+"','"+email+"','"+sub+"','"+dis+"');"

    try:
        result_proxy = connection.execute(statement)
        return render_template("index.html",successfull=True)
    except exc.IntegrityError:
        return render_template("index.html",failed=True)


@app.route('/search')
def search():
    name = request.args.get('name')

    if name == "":
        return redirect('/')

    statement = "select * from user96 where name = '"+name+"';"

    result_proxy = connection.execute(statement)
    results = result_proxy.fetchall()

    if len(results) > 0:
        return render_template("display.html",record_exists = True,results = results)
    else:
        return render_template("display.html",record_exists = False,name = name)
    

if __name__ == "__main__":
    app.run(host="127.0.0.1",port=3000)

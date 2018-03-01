from flask import Flask, request,render_template
app = Flask(__name__)
     
@app.route("/")
def hello():
    return render_template("index2.html")
     
@app.route("/echo", methods=['POST'])
def echo(): 
    name= request.form['name']
    email= request.form['email']
    sub= request.form['sub']
    dis= request.form['dis']
    return (name + email +sub +dis)
     
     
if __name__ == "__main__":
    app.run()
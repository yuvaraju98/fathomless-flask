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
    return valid(name,email,sub,dis)

@app.route("/echo2", methods=['POST'])
def echo2(): 
    item= request.form['id']
    return item

def valid(name,email,sub,dis):
    if '@' in email and all(x.isalpha() or x.isspace() for x in name) and sub and dis :
      
        return render_template("success.html")

    else:
        return render_template("fail.html")

    
    
    
    
    

   
if __name__ == "__main__":
    app.run()
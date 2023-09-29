from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def main():
  return render_template('main.html')
@app.route("/Login.html/")
def Login():
  return render_template('Login.html')
@app.route("/Products.html/")
def Products():
  return render_template('Products.html')
@app.route("/Aboutus.html/")
def Aboutus():
  return render_template('Aboutus.html')
@app.route("/main.html/")
def Home():
  return render_template('main.html')
if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)

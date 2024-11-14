from flask import Flask, render_template # ---- this is a class which will render the template and we import the flask module

app= Flask(__name__)

@app.route("/")   #---decorator
def mysite(): # function created for calling the html page
    return render_template("mysite.html")

if __name__=='__main__':
    app.run(port=5000,debug=True)

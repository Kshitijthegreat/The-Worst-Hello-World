from flask import Flask
import hello
var=hello.main()
app=Flask(__name__)
@app.route("/")
def hello(var=var):
    return var
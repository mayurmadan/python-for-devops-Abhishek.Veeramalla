#importing flask module only from flask package to make it lightweight
from flask import Flask

#below line is used to create flask application/api instance
app = Flask(__name__)

#use decorator (refer readme from same dir for details)
#here we use decorator with inbuild 'route' function to check request is on '/' path or not[in browser] for our program 
#when request is on '/' path then only another function is execute , if not then throght error
@app.route("/test")
def hello():
    return "hello word"

#define ip to allow access it on
app.run("0.0.0.0")


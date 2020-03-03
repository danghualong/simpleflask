from flask import Flask,make_response,request

app=Flask(__name__)

@app.route('/token',methods=['GET','POST'])
def echo():
    return make_response('What\'s the matter')



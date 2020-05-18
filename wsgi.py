from flask import Flask,make_response,request,jsonify

app=Flask(__name__)

@app.route('/version',methods=['GET'])
def echo():
    active_code=request.args.get('activecode')
    result={'AppProductName':'宠物医院HIS',
    'AppName':'PHMS','UpdateRequired':1,
    'AppVersion':'1.0.0.0'}
    if(active_code):
        result['AppVersion']='1.2.6.0'
    result['DownloadUrl']='{0}{1}_{2}.zip'.format('http://localhost:80/'
    ,result['AppName'],result['AppVersion'].replace('.','_'))
    return jsonify(result),200



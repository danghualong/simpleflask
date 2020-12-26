from flask import Blueprint,make_response,request
import drugstore.utils.wx_msg_builder as msg_builder

comm_bp=Blueprint('comm',__name__)

@comm_bp.route('/wx',methods=['POST'])
def echo():
    builder=msg_builder.handle_xml(request.data)
    message=builder.message()
    print(message)
    return message

@comm_bp.route('/wx',methods=['GET'])
def check_signature():
    signature = request.args['signature']
    timestamp=request.args['timestamp']
    nonce=request.args['nonce']
    echostr=request.args['echostr']
    return echostr
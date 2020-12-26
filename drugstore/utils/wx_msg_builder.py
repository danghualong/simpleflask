import xml.etree.ElementTree as et
import time

def handle_xml(data):
    if(data==None or len(data)==0):
        return None
    xmlData=et.fromstring(data)
    msgType=xmlData.find('MsgType').text
    toUserName=xmlData.find('FromUserName').text
    fromUserName=xmlData.find('ToUserName').text
    print(msgType)
    if(msgType=='text'): 
        content=xmlData.find('Content').text.encode('utf-8')
        print(content)
        return TextMessageBuilder(fromUserName,toUserName,'我们稍后会回复您，欢迎光临')
    elif(msgType=='image'):
        mediaId=xmlData.find('MediaId').text
        picUrl=xmlData.find('PicUrl').text
        return ImageMessageBuilder(fromUserName,toUserName,mediaId)
    else:
        return BaseMessageBuilder(fromUserName,toUserName)


class BaseMessageBuilder(object):
    def __init__(self,fromUserName,toUserName):
        self.fromUserName=fromUserName
        self.toUserName=toUserName
        self.content='目前不支持该服务'
    def message(self):
        strXml= """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[{Content}]]></Content>
            </xml>
            """
        return strXml.format(FromUserName=self.fromUserName,ToUserName=self.toUserName,CreateTime=int(time.time()),
       Content=self.content)

class TextMessageBuilder(BaseMessageBuilder):
    def __init__(self,fromUserName,toUserName,content):
        super(TextMessageBuilder,self).__init__(fromUserName,toUserName)
        self.content=content

class ImageMessageBuilder(BaseMessageBuilder):
    def __init__(self,fromUserName,toUserName,mediaId):
        super(TextMessageBuilder,self).__init__(fromUserName,toUserName)
        self.mediaId=mediaId

    def message(self):
        strXml= """
            <xml>
                <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
                <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
                <CreateTime>{CreateTime}</CreateTime>
                <MsgType><![CDATA[image]]></MsgType>
                <Image>
                <MediaId><![CDATA[{MediaId}]]></MediaId>
                </Image>
            </xml>
            """
        return strXml.format(FromUserName=self.fromUserName,ToUserName=self.toUserName,CreateTime=int(time.time()),
       MediaId=self.mediaId)
    
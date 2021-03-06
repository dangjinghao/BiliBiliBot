import requests
import json
import time
class session_list:
    
    '''获取私聊的json返回数据'''

    def __init__(self,SESSDATA):     
        '''传入sessdata'''   
        #self.cookie = {"SESSDATA" : SESSDATA}
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
            "cookie" : f"SESSDATA={SESSDATA}"
        }


    def getJson(self,last_time):
        '''获取json'''
        ts_str = str(int(last_time * 1000000))
        session_url = f"https://api.vc.bilibili.com/session_svr/v1/session_svr/new_sessions?begin_ts={ts_str}&build=0&mobi_app=web"
        req = requests.get(session_url,headers=self.headers)
        self.reqJson = req.json()
        #print(req.cookies)
        return self.reqJson

    def botMsgList(self):
        '''返回session的list'''
        #print(self.reqJson['data'])
        if 'session_list' in self.reqJson['data'] :
            return self.reqJson['data']['session_list']
        else:
            return None
    def cancelUnreadMsg(self,botMsglist):
        '''取消未读信息'''
        update_url = "https://api.vc.bilibili.com/session_svr/v1/session_svr/update_ack"

        for i in botMsglist:
            talker_id = i["talker_id"]
            send_data = {"talker_id":str(talker_id),"session_type":"1","ack_seqno": "",}
            if not i["unread_count"] == 0: 
                update_req = requests.post(update_url,data = send_data,headers=self.headers)

                print(f"取消与{str(talker_id)}的未读信息，返回值：" + str(update_req.json()))





class event:

    '''对传入的dict进行格式化为的一个含多信息类'''

    def __init__(self,botMsgItem):
        self.botMsgItem = botMsgItem
        #self.get_talker_id = botMsgItem['talker_id']
        self.get_last_msg_dict = botMsgItem['last_msg']
        self.get_last_msg_content = botMsgItem['last_msg']['content']
        self.get_unread_count = botMsgItem['unread_count']

   
    def raw(self):
        '''返回原始数据'''
        return self.botMsgItem

    def sender_uid(self)->str:
        '''返回对话的发送者id'''
        return str(self.botMsgItem['last_msg']['sender_uid'])
    def talker_uid(self)->str:
        '''返回对话的id'''
        return str(self.botMsgItem['talker_id'])
    def unread_count(self)->str:
        '''返回本对话的未读信息数'''
        return str(self.botMsgItem['unread_count'])
#    def last_msg_content_str(self):
#        '''返回str类型的信息内容'''
#        return self.get_last_msg_content
    def last_msg_content_dict(self):
        '''返回dict类型的信息内容'''
        
        return json.loads(self.get_last_msg_content)

    def last_msg(self)->str:
        '''返回str信息,即发送者发送的信息'''
        #if '' in
        return str(json.loads(self.get_last_msg_content)['content'])


#以下为自己写的，无法使用
# class send_msg():
#     def __init__(self,SESSDATA):
#         self.cookie = {"SESSDATA" : SESSDATA,"l":"v"}
    
#     def configs(self,sender_uid,receiver_id):
#         self.sender_uid = sender_uid
#         self.receiver_id = receiver_id
#     def content_text(self,text_type,text):
#         self.send_data = {"msg[sender_uid]":str(self.sender_uid),"msg[receiver_id]":str(self.receiver_id),"msg[receiver_type]":"1","msg[msg_type]":str(text_type),"msg[msg_status]":"0","msg[content]":r"%7B%22content%22%3A%22as%22%7D"}
#         self.send_data2 = {"msg[sender_uid]":str(self.sender_uid),"msg[receiver_id]":str(self.receiver_id),"msg[receiver_type]":"1","msg[msg_type]":str(text_type),"msg[msg_status]":"0","msg[content]": '{"url":"https://i0.hdslb.com/bfs/article/fab12e89209c434fafde721f44b7386cbbb75d02.png","height":711,"width":1204,"type":"png","original":1,"size":134}'}
        
#         #print(self.send_data)
#     def send(self):
#         send_url = "https://api.vc.bilibili.com/web_im/v1/web_im/send_msg"
#         req = requests.post(send_url,cookies= self.cookie,data=self.send_data2)

#         return req.json()
#以下由postman自动生成
class send_msg():
    def __init__(self,SESSDATA,sender_uid):
        self.headers = {
        'cookie': f'SESSDATA={SESSDATA}' ,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
        }    
        self.sender_uid = sender_uid
    def text(self,content):
        self.content = content
    def send(self,receiver_uid):
        url = "https://api.vc.bilibili.com/web_im/v1/web_im/send_msg"
        payload = {'msg[sender_uid]': '%s' %str(self.sender_uid),
        'msg[receiver_id]': '%s'%str(receiver_uid),
        'msg[receiver_type]': '1',
        'msg[msg_type]': '1',
        'msg[msg_status]': '0',
        'msg[content]': '{"content":"%s"}' %str(self.content)}

        files = []
        response = requests.request("POST", url, headers=self.headers, data = payload, files = files)
        print("向UID:"+str(receiver_uid)+"发送:"+ str(self.content))
        return response.json()




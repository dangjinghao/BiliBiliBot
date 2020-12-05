import BiliBotCore
import time
from threading import Thread

class BiliBot:
    def __init__(self,SESSDATA,uid:int):
        #self.SESSDATA = SESSDATA
        #实例化bot接收信息和发送信息
        self.bili_bot = BiliBotCore.session_list(SESSDATA)
        self.sm = BiliBotCore.send_msg(SESSDATA,uid)
        global act_func_list
        act_func_list = []

    def send_msg(self,text:str,receiver_uid):
        self.sm.text(text)
        self.sm.send(receiver_uid)


    def act_func(self,func):
        #向多线程的list中传入func
        act_func_list.append(func)        
        
    def act_return_func(self,act_func,event):
        rep = act_func(event)
        if not rep == None:
            self.send_msg(str(rep),event.talker_uid())
        
                    

    def bot(self):
        '''bot运行主体'''
        #初始ts
        ts = time.time()

        while True:
            #bot_ts = str(int(ts * 1000000))
            
            #print("目前时间戳--" + str(ts))
            print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            #格式化一个list存储event
            msg_list =[]
            self.bili_bot.getJson(ts)
            bot_msg_list = self.bili_bot.botMsgList()
            
            if not bot_msg_list == None:
                for i in bot_msg_list:
                    #遍历list，制为class
                    if not i["unread_count"] == 0:
                        #如果信息未读
                        #此为特殊情况，即起始ts到现ts之间存在未读但是并不消失，而是在“unread_count”元素下参数表为未读
                        bot_event = BiliBotCore.event(i)
                        msg_list.append(bot_event)
                        #如有未读消息，更新时间戳
                        ts = time.time()
                    else:
                        print("无新信息")
                self.bili_bot.cancelUnreadMsg(bot_msg_list)
            else:
                print("无新信息")

            for i  in msg_list:
                print("收到新event---" + str(i.raw()))
                #此处处理func
                
                for ifunc in act_func_list:
                    #多线程处理 防止func繁多阻塞
                    #self.act_return_func(ifunc,i)
                    threadgo = Thread(target=self.act_return_func, args=(ifunc,i,))
                    threadgo.start()

            time.sleep(2)




# BiliBiliBot
 用于哔哩哔哩（B站）私聊的单线程响应式机器人





## 声明
本项目仅用于开发学习，仅用于开发交流。请勿商业化，请勿商用。



## 前言
本项目基于

[SocialSisterYi/bilibili-API-collect]: https://github.com/SocialSisterYi/bilibili-API-collect	"bilibili-API-collect"



基于python3(.8.0)



本项目制作极为仓促，部分处理逻辑非常简陋，如有更好的处理方案，请提issue



目前尚未解决问题：

- [ ] 多线程装饰器
- [ ] 发送图片信息
- [ ] 支持主动式发送信息
- [ ] 发送bmoji



## 下载本项目

clone本`BiliBiliBot`库至本地，

（暂不支持通过python包管理工具下载）



## 使用本项目



导入BiliBiliBot.py

```python
import ./BiliBiliBot
```



实例化

```python
BiliBot = BiliBiliBot.BiliBot(SESSDATA = "",uid = )
#sessdata为cookie中的元素，uid为本bot的uid
```



开发者需使用装饰器以基于本项目进行开发

如果您不了解python中装饰器用法，请自行学习。



使用装饰器

```python
@BiliBiliBot.BiliBot.act_func
def sfunc(event):
    #此处让开发者执行命令
    
    
    #返回值作为对发送者的回复信息
    return event.last_msg_content_dict()
    
```



其中sfunc()函数会传入到BiliBiliBot.BiliBot.act_func()中，名称可随意：

```python
def theresaN1(event):
    
    print("德莉莎天下第一！")
    
```



event类中包含多个函数

```python
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

    def sender_uid(self):
        '''返回对话的发送者id'''
        return self.botMsgItem['last_msg']['sender_uid']
    def talker_uid(self):
        '''返回对话的id'''
        return self.botMsgItem['talker_id']
    def unread_count(self):
        '''返回对话的未读数'''
        return self.botMsgItem['unread_count']
    def last_msg_content_str(self):
        '''返回str类型的信息内容'''
        return self.get_last_msg_content
    def last_msg_content_dict(self):
        '''返回dict类型的信息内容'''
        contents = json.loads(self.get_last_msg_content)
        return contents
```



此时bot并未运行，使用以下方式运行

```python
BiliBot.bot()
```



随后bot将以两秒请求一次的方式来运行。



##  目标&&期望

- [ ] 不定期更新（5stars）
- [ ] 制为网络框架使非python开发者使用（50stars）
- [ ] 完善readme



以上。
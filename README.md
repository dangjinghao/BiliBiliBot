# BiliBiliBot
 用于哔哩哔哩（B站）私聊的多线程响应式机器人





## 声明



本项目仅用于开发学习，仅用于开发交流。请勿商业化，请勿商用。



## 前言



本项目基于（如果你没看见私聊的有关api，说明我忘记给BAC项目推送pr了233）

[SocialSisterYi/bilibili-API-collect](https://github.com/SocialSisterYi/bilibili-API-collect/ )

基于python3(.8.0)



本项目制作极为仓促，部分处理逻辑非常简陋，如有更好的处理方案，请提issue

约7~14个工作日会对issue回复。如果是较为重要的问题，可向我发送邮箱。



目前尚未解决问题：

- [x] 多线程装饰器
- [ ] 类继承
- [ ] 收发图片
- [x] 支持主动式发送信息
- [x] 发送bmoji（内部支持）



## 下载本项目



clone本`BiliBiliBot`库至本地，

（暂不支持通过python包管理工具下载）



## 使用本项目



导入BiliBiliBot.py

```python
import BiliBiliBot
```



实例化

```python
blb = BiliBiliBot.BiliBot(SESSDATA = "",uid = )
#sessdata为cookie中的元素，uid为本bot的uid
```



开发者需使用装饰器以基于本项目进行开发

如果您不了解python中装饰器用法，请自行查找资料学习。



使用装饰器

```python
@blb.act_func
def sfunc(event):
    #此处让开发者手写功能
    
    
    #返回值作为对发送者的回复信息
    return "test"
    
```



其中sfunc()函数会传入到BiliBiliBot.BiliBot.act_func()中，名称可随意：

```python
def theresaN1(event):
    
    print("德莉莎天下第一！")
    #即当接受到新信息时打印“德莉莎天下第一！”
```



主动发送信息

```python
blb.send_msg(text,receiver_uid)
```





event类中包含多个函数

| 函数                  | 描述                           |
| --------------------- | ------------------------------ |
| raw                   | 原始数据                       |
| sender_uid            | 对话的发送者id                 |
| talker_uid            | 对话id                         |
| unread_count          | 本对话未读信息数               |
| last_msg_content_dict | 返回dict类型的信息内容         |
| last_msg              | 返回str信息,即发送者发送的信息 |



此时bot并未运行，使用以下方式运行

```python
BiliBot.bot()
```



随后bot将以两秒请求一次的方式来循环运行。







##  目标&&期望

- [ ] 不定期更新
- [ ] 为非python开发者制作为网络框架
- [ ] 完善readme
- [ ] 更新日志/小型博客
- [ ] 重构，规范变量
- [ ] 二次重构，优化逻辑





以上。
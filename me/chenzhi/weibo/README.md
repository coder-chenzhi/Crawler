登录的url
http://login.weibo.cn/login/?rand=611097179&backURL=http%3A%2F%2Fweibo.cn%2F&backTitle=%E5%BE%AE%E5%8D%9A&vt=4&revalid=2&ns=1

私信的url
http://weibo.cn/msg/?tf=5_010&vt=4
页面上会显示所有对话的最新信息
如果对话很多，则需要翻页，翻页需要向
http://weibo.cn/msg/?tf=5_010&vt=4
Post mp=8&page=3

进入跟某人的具体对话列表的url
http://weibo.cn/im/chat?uid=1693756354&rl=1
每个这样的url都在<a class="cc" href=""></a>中

进入之后，所有对话都在<div class="c">的div中
但也只会显示少量信息
有一个<div class="c">中是查看更多对话的url
http://weibo.cn/im/chat?uid=1693756354&type=record&rl=2


进入之后，所有对话也都在<div class="c">的div中，
首先
mydivs = soup.findAll("div", { "class" : "c" })
获取所有div
第一个div是“返回聊天”的一个herf
第二个div有一个对方的主页herf，以及对方的昵称
剩下的都是对话
如果对话很多，则需要翻页，翻页需要向当前对话的url
Post mp=2&page=2
每个对话的div中，时间都在
<span class="ct">2013-06-12 22:26:17</span>
这样的span中
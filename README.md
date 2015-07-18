#Geek Mooc签到系统#
##需求##

* 记录每个人每天的考勤情况
* 进行简单的数据分析

##功能##

- [x] <del>使用账号登陆考勤系统</del>
- [x] <del>根据登陆时间显示可以打卡的时间段</del>
- [x] <del>显示以往的打卡记录</del>
- [ ] 登入登出操作
- [ ] 数据统计分析
- [ ] 个人资料修改

##截图##
![ ](/login.png  "login")

![](/home.png) 

##使用##
由于正在开发中，测试时可以使用`sqlit3`来生成相应的数据库：
```
python manage.py syncdb
```

##实现##

* 前端：`bootstrap`
* 后台：`Django`
* 数据库：`sqlite3`

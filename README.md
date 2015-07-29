#Geek Mooc签到系统#
##需求##

记录每个人每天的考勤情况


##功能##

- [x] <del>使用账号登陆考勤系统</del>
- [x] <del>根据登陆时间为对应时间段打卡</del>
- [x] <del>打卡时局部刷新页面</del>
- [x] <del>显示以往的打卡记录</del>
- [x] <del>各种动画</del>:)

##截图##
![ ](/login.png)

![](/clockin.png) 

![](/sheet.png) 

##使用##
测试时可以使用`sqlite3`来生成相应的数据库，并使用`south`进行迁移：
```
python manage.py schemamigration login --initial
python manage.py syncdb
python manage.py migrate login
```

##实现##

* 前端：`bootstrap`
* 脚本：`JavaScript`
* ajax支持：`jQuery`
* 后台：`Django`
* 数据库：`sqlite3`
* 数据库迁移：`south`

##写在最后##
对于*giant screen*的使用需要调整*.css*和*.js*来使得图片占满一屏。目前可以在*height: 768px*达到良好的效果。具体参见注释。

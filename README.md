# db-camera 软件介绍
db-camera是一款MySql数据库备份（快照保存）与恢复软件。功能上与dump类似，但是提供了相对有好的交互界面，能够有效地管理导出的sql文件。

# 使用场景
开发阶段、测试阶段，尤其适合单人开发的小项目。

例如开发完毕需要验证时，可以先造好准备数据，点击“保存”按钮保存数据库的快照。测试失败时，点击“执行”按钮，恢复数据库至先前的状态，重复测试。

测试人员在验证测试用例时，可以先准备好对应的前置条件，保存数据库快照。保存时可以标注用例的说明、期望结果等。
用例验证失败后，也可以保存对应的数据库快照，导出并发送给开发人员。

**注意：因为数据库的导入、导出都没有加事务控制，不可用于生产环境。**
# 界面说明

## 主界面
表格：记录历史数据库状态。点击删除按钮，删除文件；点击导出按钮，可以打开历史sql所在目录；点击执行按钮，可以恢复数据库状态。

保存：点击保存按钮，保存数据库状态。可以通过下拉框选择或搜索数据库。

设置：配置ip地址

导入：导入此软件导出的sql文件，可以读取其标题和备注信息。
![主界面图片](https://github.com/DayRain/db-camera/blob/master/img-folder/main_page.png)

## 配置页面
输入数据库的ip地址、用户、密码，因为要读取所有数据库信息，需要提供管理员权限。

配置完毕后，点击“连接测试”，测试是否配置正确。
![配置页面](https://github.com/DayRain/db-camera/blob/master/img-folder/config_page.png)

## 保存界面
选择好数据库后，点击保存按钮，弹出保存界面。输入标题以及备注的信息，点击保存。

保存后下方的表格会多出一条数据，默认新保存的数据库排在最前面。
![保存界面](https://github.com/DayRain/db-camera/blob/master/img-folder/save_page.png)
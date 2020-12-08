### ZXZJ


#### 介绍
....


#### 环境搭建
安装python3.8
```shell
[root@localhost ~]# yum -y install zlib-devel bzip2-devel openssl-devel sqlite-devel readline-devel libffi-devel gcc
[root@localhost ~]# wget https://www.python.org/ftp/python/3.8.1/Python-3.8.1.tar.xz
[root@localhost ~]# tar -Jxf Python-3.8.1.tar.xz
[root@localhost ~]# cd Python-3.8.1
[root@localhost ~]# ./configure prefix=/usr/local/python3
[root@localhost ~]# make && make install
[root@localhost ~]# ln -s /usr/local/python3/bin/python3.8 /usr/bin/python3
[root@localhost ~]# ln -s /usr/local/python3/bin/pip3.8 /usr/bin/pip3
```
#### 初始化运行环境
```shell
[root@localhost ~]# git clone https://gitee.com/frombyte_admin/fcda-server.git
[root@localhost ~]# cd zxzj
[root@localhost ~]# python3 -m venv venv
[root@localhost ~]# source venv/bin/activate
(venv) [root@localhost ~]# pip install -r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
(venv) [root@localhost ~]# python manage.py makemigrations
(venv) [root@localhost ~]# python manage.py migrate
```

#### 启动命令
```shell
(venv) [root@localhost ~]# mkdir -p /var/run/supervisor
(venv) [root@localhost ~]# supervisord -c supervisord.conf
(venv) [root@localhost ~]# supervisorctl start all                  // 开启服务
(venv) [root@localhost ~]# supervisorctl stop all                   // 关闭服务
```


# sinpy

Sinpy: Simple Single Python Web Service

使用Sinpy开发Web服务: 用最简单的架构,实现够用的框架,服务海量的用户

https://github.com/baimawen/sinpy

## Sinpy文档

## 目的

本项目采用了一系列Python中比较流行的组件, 可以以本项目为基础快速搭建Restful Web Api

## 技术栈
```Python3.7 + FastAPI + MySQL + Redis + Tortoise-orm + Aerich```

## 特色
本项目已经整合了许多开发API所必要的组件:

1. [FastAPI](https://github.com/tiangolo/fastapi):FastAPI 框架，高性能，易于学习，快速编写代码，随时可供生产


本项目已经预先实现了一些常用的代码方便参考和复用:

1. 创建了用户模型
2. 实现了```/api/v1/user/register```用户注册接口

本项目已经预先创建了一系列文件夹划分出下列模块:

1. api文件夹就是MVC框架的contrller,负责协调各部件完成任务

## Godotenv

项目在启动的时候依赖以下环境变量，但是在也可以在项目根目录创建.env文件设置环境变量便于使用(建议开发环境使用)

```shell
MYSQL_DSN="db_user:db_password@/db_name?charset=utf8&parseTime=True&loc=Local" # Mysql连接地址
REDIS_ADDR="127.0.0.1:6379" # Redis端口和地址
REDIS_PW="" # Redis连接密码
REDIS_DB="" # Redis库从0到10
SESSION_SECRET="setOnProducation" # Seesion密钥，必须设置而且不要泄露
GIN_MODE="debug"
```

## API接口文档地址

```
# host 服务器地址
http://host:8001/docs#/
http://host:8001/redoc
```


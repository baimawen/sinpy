#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/22 13:23
# @Author  : CoderCharm
# @File    : development_config.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""
开发环境配置
"""
import os

from typing import Union, Optional

from pydantic import AnyHttpUrl, BaseSettings, IPvAnyAddress


class Settings(BaseSettings):
    # 开发模式配置
    DEBUG: bool = True
    # 项目文档
    TITLE: str = "XX_API"
    VERSION="1.0.0"
    DESCRIPTION: str = "xx平台用户模块接口文档"
    # 文档地址 默认为docs
    DOCS_URL: str = "/api/docs"
    # 文档关联请求数据接口
    OPENAPI_URL: str = "/api/openapi.json"
    # redoc 文档
    REDOC_URL: Optional[str] = "/api/redoc"

    # token过期时间 分钟
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    # 生成token的加密算法
    ALGORITHM: str = "HS256"

    # 生产环境保管好 SECRET_KEY
    SECRET_KEY: str = 'aeq)s(*&(&)()WEQasd8**&^9asda_asdasd*&*&^+_sda'

    # 项目根路径
    BASE_PATH: str = os.path.dirname(os.path.dirname(os.path.dirname((os.path.dirname(os.path.abspath(__file__))))))

    # 配置你的Mysql环境
    MYSQL_USERNAME: str = ""
    MYSQL_PASSWORD: str = ""
    MYSQL_HOST: Union[AnyHttpUrl, IPvAnyAddress] = ""
    MYSQL_POET: int = 3306
    MYSQL_DATABASE: str = ''

    # Mysql地址
    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@" \
                              f"{MYSQL_HOST}/{MYSQL_DATABASE}?charset=utf8mb4"

    # redis配置
    REDIS_HOST: str = ""
    REDIS_PASSWORD: str = ""
    REDIS_DB: int = 0
    REDIS_PORT: int = 6379
    REDIS_URL: str = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}?encoding=utf-8"


settings = Settings()

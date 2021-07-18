# -*- coding: utf-8 -*-
# @Time    : 2021/4/22 15:17
# @Author  : #
# @File    : models.py
# @Software: PyCharm
# ./models.py
import sqlalchemy
from sqlalchemy import INTEGER, Column, ForeignKey, String, FLOAT, DateTime
from sqlalchemy.orm import declarative_base, relationship
from tools.auth import JWTencode

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True


class Game(BaseModel):
    __tablename__ = "game"
    gid = Column(INTEGER(), primary_key=True)
    game = Column(String())

    def to_dict(self):
        data = {
            "gid": self.gid,
            "game": self.game
        }
        return data


class User(BaseModel):
    __tablename__ = "user"
    uid = Column(INTEGER(), primary_key=True)
    username = Column(String())
    password = Column(String())
    auth = Column(String())

    async def to_dict(self, secret, exist_time):
        data = {"username": self.username, "uid": self.uid, "auth": self.auth}
        token = await JWTencode(data.copy(), secret, exist_time)
        data.update({"token": token})
        return data


class User_Game(BaseModel):
    __tablename__ = "user_game"
    id = Column(INTEGER(), primary_key=True)
    uid = Column(INTEGER(), ForeignKey("user.uid"))
    gid = Column(INTEGER(), ForeignKey("game.gid"))

    def to_dict(self):
        data = {
            "uid": self.uid,
            "gid": self.gid
        }
        return data


class Roles(BaseModel):
    __tablename__ = "roles"
    rid = Column(INTEGER(), primary_key=True)
    data = Column(String())
    gid = Column(INTEGER(), ForeignKey("game.gid"))

    def to_dict(self):
        data = {
            "data": [{"name": i.split(",")[0], "img": i.split(",")[1]} for i in self.data.split("----")],
            "gid": self.gid
        }
        return data


class Account(BaseModel):
    __tablename__ = "account"
    aid = Column(INTEGER(), primary_key=True)
    uid = Column(INTEGER(), ForeignKey("user.uid"))
    gid = Column(INTEGER(), ForeignKey("game.gid"))
    number = Column(String())
    goods = Column(String())
    info_hidden = Column(String())
    info_show = Column(String())
    price = Column(FLOAT())
    img = Column(String())

    def to_dict(self, show_hidden):
        data = {
            "aid": self.aid,
            "uid": self.uid,
            "gid": self.gid,
            "number": self.number,
            "goods": [i for i in self.goods.split(',')],
            "info_hidden": self.info_hidden if show_hidden else "",
            "info_show": self.info_show,
            "price": self.price,
            "img": self.img.split(',')
        }
        return data

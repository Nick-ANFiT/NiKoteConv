#!/usr/bin/python
# -*- coding: utf-8 -*-
# okayu-ser.py - a program to print list user id and handle name from Okayu.
# Copyright (C) 2015 by Nick@ANFiT Productions.
#

import os
import sqlite3
import types

# Viqo のコテハンが保存されている DBを指定する。
viqodb = os.path.expanduser('~/Library/Application Support/Viqo/user.sqlite')

# DB が存在しなければ終了する。
if not os.path.exists(viqodb):
    exit()

# DB を開く
con = sqlite3.connect(viqodb)
c = con.cursor()
# DB からニコ生のユーザーIDとコテハンを取得する。
c.execute(u"select id, name from user")
for row in c:
    # 取得したコテハンを表示する為に、文字列をエンコードする。
    if isinstance(row[1], unicode):
        ns = row[1].encode('utf-8')
    else:
        ns = row[1]
    # DB から取得したニコ生のユーザーIDとコテハンを表示する。
    print row[0],"\t",ns

# DB関係の後処理
c.close
con.close

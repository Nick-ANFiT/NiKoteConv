#!/usr/bin/python
# -*- coding: utf-8 -*-
# okayu-ser.py - a program to print list user id and handle name from Okayu.
# Copyright (C) 2015 by Nick@ANFiT Productions.
#

import os
import sqlite3
import types

# Okayu のコテハンが保存されている DBを指定する。
okayudb = os.path.expanduser('~/Library/Application Support/Okayu/okayu.sqlite3')

# DB が存在しなければ終了する。
if not os.path.exists(okayudb):
    exit()

# DB を開く
con = sqlite3.connect(okayudb)
c = con.cursor()
# DB からニコ生のユーザーIDとコテハンを取得する。
c.execute(u"select code, name from users")
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

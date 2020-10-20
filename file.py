#!/usr/bin/env python
# coding=utf-8


# File base operation

Sym = ('*')





Hlist = []

Hlist = open('./myInfo.txt').readlines()

for x in Hlist:
    print Sym * 79
    print (x)

#!/usr/bin/env python
# coding=utf-8


print "Start our second class!"


Str = "imSPAMaSPAMlumberjack"

Str1 = Str.split("SPAM")

print Str1

Str2 = "ChicagofuckNewYorkfuckBoston"
str3 = Str2.split("fuck")

print str3

Vechile = "THe knight who say Ni!\n"
sub = "Ni!\n"

V1 = Vechile.rstrip()
V2 = Vechile.endswith("kelly")
V3 = Vechile.startswith("The")
V4 = Vechile.find("knight") != -1

print Vechile[-len(sub):] == sub


Name = "Augustine"
Age = 36

print "His name is %s, he is %d" % (Name, Age)























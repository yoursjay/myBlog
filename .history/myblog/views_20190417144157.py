#!/usr/bin/env python
# coding=UTF-8
'''
@Author: JayLee
@Github: https://github.com/yoursjay
@LastEditors: Jay
@Date: 2019-04-17 14:41:06
@LastEditTime: 2019-04-17 14:41:09
'''
from django.shortcuts import render

def home(request):
    return render(request,'home.html')
#!/usr/bin/env python
# coding=UTF-8
'''
@Author: JayLee
@Github: https://github.com/yoursjay
@LastEditors: Jay
@Date: 2019-04-17 14:41:06
@LastEditTime: 2019-04-17 15:18:51
'''
from django.shortcuts import render
from gallery.models import Gallery

def home(request):
    gallerys = Gallery
    return render(request,'home.html',{'gallerys':gallerys})
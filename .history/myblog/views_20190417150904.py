#!/usr/bin/env python
# coding=UTF-8
'''
@Author: JayLee
@Github: https://github.com/yoursjay
@LastEditors: Jay
@Date: 2019-04-17 14:41:06
@LastEditTime: 2019-04-17 15:09:04
'''
from django.shortcuts import render
from gallery.models import Gallery

def home(request):
    gallerys = Gallery.description
    return render(request,'home.html',{'gallerys':gallerys})
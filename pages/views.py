# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def home(request):
    print(request)
    context = {}
    return render(request, 'base.html', context)

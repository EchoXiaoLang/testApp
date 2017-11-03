# -*- coding: utf-8 -*-

from common.mymako import render_mako_context
from django.contrib.auth import authenticate
from django.db import models


def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')

def dev_work(request):
    user = authenticate(request=request)
    id   =user.id
    work_uer=models.Model.objects.get(pk=id);
    return render_mako_context(request, '/home_application/resume.html',{'work_uer':work_uer})

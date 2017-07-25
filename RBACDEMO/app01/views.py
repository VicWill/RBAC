from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from rbac.service import initial_permission


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        print(user, pwd)
        obj = models.UserInfo.objects.filter(user__username=user, user__password=pwd).first()
        print(obj)
        if obj:
            initial_permission(request, obj.user.id)
            return redirect('/index.html')
        else:
            return render(request, 'login.html', {'msg': '用户名或密码错误'})


def register(request):
    return render(request, 'register.html')


def logout(request):
    request.session.clear()
    request.session.delete()
    return redirect('/login.html')


def index(request):
    return render(request, 'index.html')


def order(request):
    print(request.permission_code)       # 当前用户以什么权限访问当前URL
    print(request.permission_code_list)  # 当前用户对当前URL所具有的所有权限

    if request.permission_code == "GET":
        # 查看权限
        pass
    elif request.permission_code == "POST":
        # 添加权限
        pass
    elif request.permission_code == "PUT":
        # 修改权限
        pass
    elif request.permission_code == "DELETE":
        # 删除权限
        pass

    return HttpResponse('订单')



from django.shortcuts import render, redirect, HttpResponse

from web import models
from rbac.service import initial_permission


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        u = request.POST.get('username')
        p = request.POST.get('password')
        obj = models.UserInfo.objects.filter(user__username=u, user__password=p).first()
        if obj:
            request.session['user_info'] = {'username': u, 'nickname': obj.nickname, 'nid': obj.id}
            initial_permission(request, obj.user_id)
            return redirect('/index.html')
        else:
            return render(request, 'login.html')


def index(request):
    if not request.session.get('user_info'):
        return redirect('/login.html')

    return render(request, 'index.html')


def trouble(request):

    if request.permission_code == 'LOOK':
        trouble_list = models.Order.objects.filter(create_user_id=request.session['user_info']['nid'])

        return render(request, 'trouble.html', {'trouble_list': trouble_list})

    elif request.permission_code == 'DEL':
        nid = request.Get.get('nid')
        models.Order.objects.filter(create_user_id=request.session['user_info']['nid'], id=nid).delete()
        return redirect('/trouble.html')

    elif request.permission_code == 'POST':
        if request.method == "GET":
            return render(request, 'trouble_add.html')
        else:
            title = request.POST.get('title')
            content = request.POST.get('content')
            models.Order.objects.create(title=title, detail=content, create_user_id=request.session['user_info']['nid'])
            return redirect('/trouble.html')




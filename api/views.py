from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    if request.POST["username"] == "test" and request.POST["pwd"] == "123456":
        result = {'code': 0, 'msg': '登录成功'}
        request.session["username"] = request.POST["username"]
    else:
        result = {'code': 0, 'msg': '登录失败'}
    return JsonResponse(result)


def get_shop_list(request):
    username = request.session.get("username")
    if username:
        # result = {'code': 0, 'data': [{"id": 1001, "name": "橘子"}, {"id": 1002, "name": "哈密瓜"}], "msg": "请求成功"}
        result = [{'code': 0, 'data': [{"id": 1001, "name": "橘子"}, {"id": 1002, "name": "哈密瓜"}], "msg": "请求成功"}]
    else:
        result = {'code': -1, 'msg': '登录失败'}
    return JsonResponse(result, safe=False)


@csrf_exempt
def save_shop(request):
    username = request.session.get("username")
    if username:
        result = {"code": 0, "msg": "提交成功",  'data': [{"id": 1002, "name": "橙子"}, {"id": 1002, "name": "西瓜"}]}
    else:
        result = {'code': -1, 'msg': '登录失败'}

    return JsonResponse(result)
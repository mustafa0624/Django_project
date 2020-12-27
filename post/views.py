from django.shortcuts import render,HttpResponse


def post_index(req):
    return HttpResponse("index sayfasi")

def post_detail(req):
    return HttpResponse("detail sayfasi")

def post_create(req):
    return HttpResponse("create sayfasi")

def post_update(req):
    return HttpResponse("update sayfasi")

def post_delete(req):
    return HttpResponse("delete sayfasi")

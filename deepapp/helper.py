from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse

def renderhelper(request,folder,htmlpage,context={}):
    return render(request,'superadmin/'+folder+'/'+htmlpage+'.html',context)

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

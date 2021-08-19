from django.shortcuts import render

# Create your views here.
def loop(request):
    d={'name':'ashu'}
    return render(request,'loop.html',context=d)
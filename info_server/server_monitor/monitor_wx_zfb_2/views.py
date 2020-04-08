from django.shortcuts import render

# Create your views here.
def index(request):
    req = {}
    test = 'bbb'
    print(test)
    return render(request, 'monitor_wx_zfb_2/index.html', req)

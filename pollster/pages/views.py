from django.shortcuts import render
#from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'pages/index.html')
# Create your views here.

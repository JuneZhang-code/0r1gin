from django.shortcuts import render

# Create your views here.
def community(request):
    return render(request,'Community/community.html')

def invest(request):
    return render(request,'Community/invest.html')

def started(request):
    return render(request,'Community/started.html')

def question(request):
    return render(request,'Community/question.html')

def interest(request):
    return render(request,'Community/interest.html')

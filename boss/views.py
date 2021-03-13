from django.shortcuts import render
from django.http import HttpResponse

appointments = [
    {
        'title': 'Job application',
        'content': 'this is regarding a hiring post',
    },
    {
        'title': 'Second application',
        'content': 'this is second job application',
    }
]


def home(request):
    context = {
        'appointments': appointments
        # it can be a t*ry name , can change it to appoint
    }
        # a = get_object_or_404('', pk=pk)
    return render(request, 'template/home.html', context)




# Create your views here.

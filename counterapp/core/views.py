from django.shortcuts import render, redirect
from .models import Click

# Create your views here.


def home(request):

    click = Click.objects.first()
    if not click:
        click = Click.objects.create()

    if request.method == 'POST':
        print (click)
        click.counter += 1
        click.save()
        return redirect('/')
    else:
        click = Click.objects.first()
        context = {
            'counter': click
        }
        return render(request, 'home.html', context)
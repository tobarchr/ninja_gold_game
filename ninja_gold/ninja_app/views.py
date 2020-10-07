from django.shortcuts import render, redirect
import random
from datetime import datetime,timezone


def index(request):
    if 'coins' not in request.session:
        request.session['coins'] = 0
        request.session['log'] = ''
    return render(request, "index.html")


def processed(request):
    now = datetime.now() # current date and time
    if request.POST['which_form'] == 'farm':
        tokens = random.randint(10,20)
        request.session['coins'] += tokens
        console = "\nEarned " + str(tokens) + " from the farm! " + now.strftime("(%m/%d/%Y %H:%M:%S)")
        request.session['log'] += console
        time= datetime.now(timezone.utc)
        print(timezone.utc)
    if request.POST['which_form'] == 'cave':
        tokens = random.randint(5,10)
        request.session['coins'] += tokens
        console = "\nEarned " + str(tokens) + " from the cave! " + now.strftime("(%m/%d/%Y %H:%M:%S)")
        request.session['log'] += console
    if request.POST['which_form'] == 'house':
        tokens = random.randint(2,5)
        request.session['coins'] += tokens
        console = "\nEarned " + str(tokens) + " from the house! " + now.strftime("(%m/%d/%Y %H:%M:%S)")
        request.session['log'] += console
    if request.POST['which_form'] == 'casino':
        tokens = random.randint(-50,50)
        request.session['coins'] += tokens
        if (tokens < 0):
            console = "\nEntered a casino and lost " + str(tokens) + " golds... Ouch.."  + now.strftime("(%m/%d/%Y %H:%M:%S)")
            request.session['log'] += console
        else:
            console = "\nEarned " + str(tokens) + " from the casino! "  + now.strftime("(%m/%d/%Y %H:%M:%S)")
            request.session['log'] += console
    return redirect('/')


def delete(request):
    del request.session['coins']  
    del request.session['log'] 
    return redirect('/')
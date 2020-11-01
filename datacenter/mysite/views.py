from django.shortcuts import render
from django.http import HttpResponse
import random

def index(request):
    lucky_num = random.randint(1,42)
    numbers = list()
    for i in range(6):
        numbers.append(random.randint(1,42))
    #return HttpResponse("<h1>your lucky number is {}</h1>".format(lucky_num))
    return render(request, "index.html", locals())
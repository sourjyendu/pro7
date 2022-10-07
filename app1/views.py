from calendar import c
import re
from django.shortcuts import render

# Create your views here.
def maxx(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'greater.html',context=d)
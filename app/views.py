from django.shortcuts import render,HttpResponse
import requests


from . models import *

def index(request):
        url = "https://api.dictionaryapi.dev/api/v2/entries/en/dog"
        data=requests.get(url).json()
        mp3=data[0]
        print(mp3)
        return render(request,"index.html")

def get(request):
    song=request.POST['Song']
    try:
        url = "https://api.dictionaryapi.dev/api/v2/entries/en/song"
        data=requests.get(url)
        print(data[origin])
        return render(request,'index.html',{"data":data})

    except:
        return HttpResponse("<center><h1>Song not found go back and try check again</h1></center>")
    

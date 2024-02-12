from django.shortcuts import render, redirect
from .models import Sortener
import pyshorteners
from django.http import HttpResponse



def index(request):
    x = Sortener.objects.all()
    shortener = pyshorteners.Shortener()
    if request.method == 'POST':
        new_url = Sortener(
            long_urls = request.POST.get('url'),
            short_urls = shortener.tinyurl.short(request.POST.get('url')),
        )
        new_url.save()
        return redirect('index')
    return render(request, 'index.html', {'x':x})
    

def stats(request, url):
    shortner = Sortener.objects.get(short_urls=url)
    if request.method == 'POST':
        shortner.views_count += 1
        shortner.save()
        return redirect(shortner.short_urls)
    return render(request, 'statistiks.html', {'shortner':shortner})





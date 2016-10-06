from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Album
from django.template import loader
# Create your views here.
def index(request):
	all_albums = Album.objects.all()
	print all_albums
	context = {
		"all_albums" : all_albums,
	}
	return render(request, 'music/index.html', context)

def details(request, album_id):
	try:
		album = Album.objects.get(pk=album_id)
		context = {
			"album_id" : album_id,
			"album_title" : album.album_title,
		}
		return render(request, 'music/details.html', context)
	except:
		raise Http404()

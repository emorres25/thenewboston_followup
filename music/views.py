from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Album, Song
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
			"album" : album,
		}
		return render(request, 'music/details.html', context)
	except:
		raise Http404()

def favorite(request, album_id):
	album = Album.objects.get(pk=album_id)
	try:
		selected_song = album.song_set.get(pk=request.POST['song'])
	except:
		error_msg = "Something went wrong"
		context = {
			"error_msg" : error_msg,
		}
		return render(request, "music/details.html", context)
	else:
		selected_song.is_favorite = False
		selected_song.save()

		return render(request, "music/details.html", {'album' : album})